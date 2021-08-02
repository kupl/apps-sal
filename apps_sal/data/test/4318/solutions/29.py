n = int(input())
h = [int(s) for s in input().split()]
highest = h[0]
ans = 1
for i in range(1, n):
    if h[i] >= highest:
        ans += 1
        highest = h[i]
print(ans)
