N, M = map(int, input().split())
conflicts = [list(map(int, input().split())) for i in range(M)]

intervals = []
for conflict in conflicts:
    intervals.append([conflict[0], conflict[1] - 1])

intervals = sorted(intervals, key=lambda x: x[1])

count = 0
end = -float("inf")
for interval in intervals:
    if interval[0] > end:
        count += 1
        end = interval[1]

print(count)
