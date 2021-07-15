n, k = list(map(int,input().split()))
h = []

for i in range(n):
    x = int(input())
    h.append(x)

h = sorted(h)
ans = 10**9
tmp = 0

for i in range(k-1, n):
    tmp = h[i] - h[i-(k-1)]
    if tmp < ans:
        ans = tmp

print(ans)

