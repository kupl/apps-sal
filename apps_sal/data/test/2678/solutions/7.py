N = int(input())
intervals = []
for i in range(N):
    intervals.append(list(map(int, input().split()))[-1::-1])

intervals.sort()
mx = intervals[0][0]
count = 1
for i in range(1, N):
    if intervals[i][1] > mx:
        count += 1
        mx = intervals[i][0]
print(count)
