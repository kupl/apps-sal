import os
s = input().split(' ')
n = int(s[0])
b = int(s[1])
requests = [[]] * n
for i in range(n):
    s = input().split(' ')
    requests[i] = [int(s[0]), int(s[1])]
result = [0] * n
counter = 1
time = 0
queue = []
time = requests[0][0]
queue = [[0, requests[0][1]]]
while counter < n:
    if len(queue) != 0:
        if queue[0][1] <= requests[counter][0] - time:
            time += queue[0][1]
            result[queue[0][0]] = str(time)
            queue = queue[1:]
        else:
            queue[0][1] -= requests[counter][0] - time
            time = requests[counter][0]
            if len(queue) < b + 1:
                queue += [[counter, requests[counter][1]]]
            else:
                result[counter] = '-1'
            counter += 1
    else:
        time = requests[counter][0]
        queue += [[counter, requests[counter][1]]]
        counter += 1
for i in range(len(queue)):
    time += queue[i][1]
    result[queue[i][0]] = time
print()
s = ''
for i in range(len(result)):
    s += str(result[i]) + ' '
print(s)
