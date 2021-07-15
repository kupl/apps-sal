T = int(input())

def solve():
    S = input()
    total_0 = 0
    total_1 = 0

    for i in range(len(S)):
        if S[i] == '0':
            total_0 += 1
        else:
            total_1 += 1
    ans = len(S)
    count_0, count_1 = 0,0
#    print(total_0,total_1)
    for i in range(len(S)):
        # all 0 then all 1
        ans01 = count_1 + (total_0-count_0)
        # all 1 then all 0
        ans10 = count_0 + (total_1-count_1)

        if S[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

        ans = min(ans,ans01,ans10)
    print(ans)

for _ in range(T):
    solve()

