N = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
timings = []
for i in range(N):
    timings.append([l1[i], l2[i]])

#timings = sorted(timings, key=lambda x :x[0])

end = timings[0][1]
tasks = [0]
for i in range(1, len(timings)):
    if(timings[i][0] >= end):
        end = timings[i][1]
        tasks.append(i)

print(*tasks)
