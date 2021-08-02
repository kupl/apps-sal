N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
m = min(N, K)
H = H[:N - m]
ans = 0
for i in range(len(H)):
    ans += H[i]
print(ans)
