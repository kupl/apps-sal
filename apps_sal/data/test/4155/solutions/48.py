n = int(input())
h = [int(i) for i in input().split()]


ans = h[0]

climb = 1
for i in range(1, n):
    if h[i] - h[i - 1] >= 0:
        ans += h[i] - h[i - 1]
print(ans)
