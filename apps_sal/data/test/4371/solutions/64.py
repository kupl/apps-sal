s = list(map(str, input()))
t = len(s)
i = 0
l = []
for _ in range(t - 3):
    for _ in s:
        if i <= t - 3:
            x = s[i] + s[i + 1] + s[i + 2]
            l.append(x)
        i += 1
tmp = []
for num in l:
    y = abs(int(num) - 753)
    tmp.append(y)
print(min(tmp))
