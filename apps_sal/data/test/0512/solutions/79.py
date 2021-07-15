import sys

N = int(input())
events = [(0, False)] * 2 * N
for i in range(1,N+1):
    A, B = list(map(int, input().split()))
    if A != -1:
        if events[A - 1][0] != 0:
            print('No')
            return
        events[A-1] = (i, B!=-1) # 人のid, 降りる場所が決まってるか
    if B != -1:
        if events[B - 1][0] != 0:
            print('No')
            return
        events[B - 1] = (-1 * i, A != -1)  # 人のid, のる場所が決まってるか
    if A != -1 and B != -1 and B <= A:
        print('No')
        return

def judge(l, r):
    if l % 2 != 0 or r % 2 != 0:
        return False
    d = (r - l) // 2
    for i in range(l, l + d):
        l_id, l_flg = events[i]
        r_id, r_flg = events[i + d]
        if l_flg or r_flg:
            if (l_id != -1*r_id):
                return False
        if l_id != 0 and r_id != 0:
            if l_id != -1*r_id:
                return False
        if r_id > 0:
            return False
        if l_id < 0:
            return False
    return True


dp = [False] * (N+1) # 2*iまでの区間で矛盾なく、かつ地点2*iで人を一人も載せないようにできるか
dp[0] = True
for i in range(N + 1):
    if dp[i]:
        for j in range(i + 1, N + 1):
            if judge(2 * i, 2 * j):
                dp[j] = True

if dp[-1]:
    print('Yes')
else:
    print('No')

