n = int(input())
a = list(map(int, input().split()))
cur = 0
prev = 0
for t in a:
    if t - prev > 15:
        break
    cur = t
    prev = t
cur = min(cur + 15, 90)
print(cur)

