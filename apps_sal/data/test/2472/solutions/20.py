import numpy
N = int(input())
task = numpy.array([list(map(int, input().split())) for _ in range(N)])
task = task[numpy.argsort(task[:, 1])]
ans = 'Yes'
time = 0
for j in task:
    time += j[0]
    if time > j[1]:
        ans = 'No'
        break
print(ans)
