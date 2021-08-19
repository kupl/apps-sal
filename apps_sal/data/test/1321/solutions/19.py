st = int(input())
summa = 0
q = []
w = []
ish = []
for i in range(st):
    (z, x) = map(int, input().split())
    q.append(z)
    w.append(x)
    ish.append(x)
summa = sum(q)
w.sort()
for i in range(st):
    qw = w[st - 1]
    if ish[i] == qw:
        qw = w[st - 2]
    print((summa - q[i]) * qw, end=' ')
