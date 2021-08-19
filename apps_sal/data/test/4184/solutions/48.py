N = int(input())
W = list(map(int, input().split()))
ans = 10000
l = 0
r = sum(W)
for i in range(N):
    l += W[i]
    r -= W[i]
    ans = min(abs(r - l), ans)
print(ans)
