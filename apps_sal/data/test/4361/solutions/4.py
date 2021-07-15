n, k = list(map(int, input().split()))
h = [int(input()) for i in range(n)]
h.sort()
ans = []
for i in range(n - k + 1):
    ans.append(h[i + k - 1] - h[i])
print((min(ans)))

