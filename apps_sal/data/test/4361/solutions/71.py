n, k = list(map(int, input().split()))

h = [int(input()) for _ in range(n)]

h.sort()

s = h[-1] - h[1]

for i in range(n-k+1):
    s = min(s, h[i+k-1]-h[i])

print(s)

