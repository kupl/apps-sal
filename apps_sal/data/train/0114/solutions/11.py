import sys
input = sys.stdin.readline
T = int(input())
Ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    PS = [list(map(int, input().split())) for _ in range(M)]
    L = [0] * (N + 1)
    for p, s in PS:
        L[s] = max(L[s], p)
    for i in range(N - 1, -1, -1):
        L[i] = max(L[i], L[i + 1])
    ans = 1
    cnt = 1
    ma = 0
    if L[1] < max(A):
        Ans.append(-1)
        continue
    for a in A:
        ma = max(ma, a)
        if L[cnt] < ma:
            cnt = 1
            ans += 1
            ma = a
        cnt += 1
    Ans.append(ans)

print("\n".join(map(str, Ans)))
