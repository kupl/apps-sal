our = []
for i in range(int(input())):
    s = input()
    our.append(int(s[0:2]) * 60 + int(s[3:]))
our.sort()
our.append(our[0] + 24 * 60)
res = 0
for i in range(len(our) - 1):
    res = max(res, our[i + 1] - our[i])
res -= 1
hour = str(res // 60)
minute = str(res % 60)
if len(hour) < 2:
    hour = '0' + hour
if len(minute) < 2:
    minute = '0' + minute
print(hour + ':' + minute)
