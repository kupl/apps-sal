n = int(input())
s = {}
for i in range(n):
    q = input()
    if q[0] in list(s.keys()):
        s[q[0]] += 1
    else:
        s[q[0]] = 1
u = []
ans = 0
for i in list(s.keys()):
    k = s[i]
    u.append(k)
    a = k // 2
    b = k - a
    ans += (a - 1) * a // 2 + (b - 1) * b // 2
print(ans)
