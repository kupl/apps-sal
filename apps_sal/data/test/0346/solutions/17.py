from operator import itemgetter


def R():
    return list(map(int, input().split()))


(n, m) = R()
a = list(R())
b = [0] * n
for i in R():
    b[i - 1] = 1
a = sorted(enumerate(a), key=itemgetter(1), reverse=True)
s = sum((x for (i, x) in a if b[i] != 1))
for (i, x) in a:
    if b[i] == 1:
        s += s if s > x else x
print(s)
