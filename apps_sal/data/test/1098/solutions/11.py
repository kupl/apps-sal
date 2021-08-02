n = int(input())
time = [None] * n
for i in range(n):
    t = input()
    h, m = t.split(':')
    h, m = int(h), int(m)
    num = h * 60 + m
    time[i] = num
time.sort()
time.append(time[0] + 1440)
ans = (time[1] - time[0] - 1)
for i in range(i + 1):
    ans = max(ans, time[i + 1] - time[i] - 1)
print('{:02d}:{:02d}'.format(*divmod(ans, 60)))
