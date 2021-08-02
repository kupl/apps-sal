I = lambda: list(map(int, input().split()))
I()
dic = {}
s = 0
for a in I():
    s += a
    dic[a] = dic.get(a, 0) + 1
for _ in [0] * I()[0]:
    b, c = I()
    s += (c - b) * dic.get(b, 0)
    dic[c] = dic.get(c, 0) + dic.get(b, 0)
    dic[b] = 0
    print(s)
