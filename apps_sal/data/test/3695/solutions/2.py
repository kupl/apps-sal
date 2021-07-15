n, T = map(int, input().split())

ts = list(map(int, input().split()))

intervals = []

for i in range(n):
    start = max(0, ts[i] - i - 1)
    end = T - i - 2
    
    if start > end:
        continue
    
    intervals.append((start, -1))
    intervals.append((end, 1))

intervals.sort()

ans = 0
current = 0

for _, val in intervals:
    current -= val
    ans = max(ans, current)

print(ans)
