(N, *B) = list(map(int, open(0).read().split()))
ans = B[0] + B[-1]
for i in range(N - 2):
    ans += min(B[i], B[i + 1])
print(ans)
