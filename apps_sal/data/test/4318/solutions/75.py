n = int(input())
h = list(map(int, input().split()))

ans = 0
highest = 0
for height in h:
    highest = max(height, highest)
    if height >= highest:
        ans += 1

print(ans)
