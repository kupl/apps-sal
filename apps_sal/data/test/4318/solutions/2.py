n = int(input())
h = list(map(int, input().split()))

x = 1
ans = h[0]

for i in range(1, n):
    if h[i] >= ans:
        x = x + 1
        ans = h[i]

print(x)
