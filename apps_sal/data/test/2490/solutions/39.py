s = '0' + input()
m = len(s)
up = 0
cnt = 0
y = []
for i in range(-1, -m - 1, -1):
    cs = int(s[i]) + up
    if cs < 5 or (cs == 5 and int(s[i - 1]) < 5):
        cnt += cs
        y.append([cs, s[i]])
        up = 0
    else:
        cnt += 10 - cs
        y.append([10 - cs, s[i]])
        up = 1
print(cnt)
