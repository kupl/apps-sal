b = int(input())
times = []
line = ''
a = b
while a > 0:
    a -= 1
    curr_time = input().split(':')
    times.append(int(curr_time[0]) * 60 + int(curr_time[1]))
times.sort()
times.append(times[0] + 24 * 60)
max_delta = 0
if times[0] > max_delta:
    max_delta = times[0]
for it in range(1, b + 1):
    if times[it] - times[it - 1] > max_delta:
        max_delta = times[it] - times[it - 1] - 1
if max_delta // 60 < 10:
    first = '0' + str(max_delta // 60)
else:
    first = str(max_delta // 60)
if max_delta - 60 * (max_delta // 60) < 10:
    second = '0' + str(max_delta - 60 * (max_delta // 60))
else:
    second = str(max_delta - 60 * (max_delta // 60))
print(first + ':' + second)
