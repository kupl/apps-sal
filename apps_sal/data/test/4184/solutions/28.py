N = int(input())
W = list(map(int, input().split()))
ans = []
for i in range(N - 1):
    (ans1, ans2) = (0, 0)
    for k in range(i + 1):
        ans1 += W[k]
    for k in range(i + 1, N):
        ans2 += W[k]
    ans.append(abs(ans1 - ans2))
print(min(ans))
