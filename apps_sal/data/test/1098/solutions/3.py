n = int(input())
day = 24 * 60
v = []
for i in range(n):
    s = input()
    h = int(s[0]) * 10 + int(s[1])
    m = int(s[3]) * 10 + int(s[4])
    tim = h * 60 + m
    v.append(int(tim))
    v.append(int(tim + day))
    v.append(int(tim + day + day))
v.sort()
ans = 0
for i in range(len(v)):
    if i > 0:
        ans = max(ans, v[i] - v[i - 1] - 1)
m = ans % 60
h = ans // 60
print(str(h // 10) + str(h % 10) + ':' + str(m // 10) + str(m % 10))
