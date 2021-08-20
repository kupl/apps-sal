N = int(input())
W = list(map(int, input().split()))
ans = 200
for t in range(N):
    S1 = sum(W[:t])
    S2 = sum(W[t:])
    d = abs(S1 - S2)
    if ans > d:
        ans = d
print(ans)
