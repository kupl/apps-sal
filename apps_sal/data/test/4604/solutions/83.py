N = int(input())
MOD = 10**9 + 7
A = [int(x) for x in input().split()]
flag = 1
set1 = set()
set2 = set()
if N % 2 == 1:
    set1.add(0)
    for j in range(2, N + 1, 2):
        set1.add(j)
        set2.add(j)
    for i in range(N):
        now = A[i]
        if now in set1:
            set1.remove(now)
        elif now in set2:
            set2.remove(now)
        else:
            flag = 0
            break
    if len(set1) != 0 or len(set2) != 0:
        flag = 0
else:
    for k in range(1, N + 1, 2):
        set1.add(k)
        set2.add(k)
    for p in range(N):
        now = A[p]
        if now in set1:
            set1.remove(now)
        elif now in set2:
            set2.remove(now)
        else:
            flag = 0
            break
    if len(set1) != 0 or len(set2) != 0:
        flag = 0
if flag == 0:
    print((0))
else:
    ans = 1
    div2 = N // 2
    for q in range(div2):
        ans *= 2
        ans %= MOD
    print(ans)
