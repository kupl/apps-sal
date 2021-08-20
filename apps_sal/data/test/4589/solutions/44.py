(h, w) = list(map(int, input().split()))
s = list()
t = list()
a = [0 for i in range(w + 2)]
s.append(a)
for i in range(h):
    b = str(input())
    c = list(('0' + b + '0').replace('.', '0').replace('#', '1'))
    d = list(map(int, c))
    s.append(d)
    t.append(b)
s.append(a)
for j in range(1, h + 1):
    for k in range(1, w + 1):
        if s[j][k] == 0:
            cnt = 0
            cnt = s[j - 1][k - 1] + s[j - 1][k] + s[j - 1][k + 1] + (s[j][k - 1] + s[j][k + 1]) + (s[j + 1][k - 1] + s[j + 1][k] + s[j + 1][k + 1])
            t[j - 1] = t[j - 1].replace('.', str(cnt), 1)
        else:
            continue
for i in range(h):
    print(t[i])
