n = int(input())
c = []
s = []
f = []
for i in range(n - 1):
    c_, s_, f_ = map(int, input().split())
    c.append(c_)
    s.append(s_)
    f.append(f_)

for i in range(n - 1):
    res = s[i] + c[i]
    for j in range(i + 1, n - 1):
        if res >= s[j]:
            if (res - s[j]) % f[j] == 0:
                res = res + c[j] + ((res - s[j]) % f[j])
            else:
                res = res + c[j] + f[j] - ((res - s[j]) % f[j])
        else:
            res = s[j] + c[j]
    print(res)
print(0)
