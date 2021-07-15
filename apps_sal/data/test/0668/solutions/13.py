from operator import itemgetter

n = input()
n = int(n)
a = str()

a = input()
a = a.split()
a = list(map(int, a))

asum = sum(a)

if a[0] == 0 or asum < n - 1:
    print(-1)
    return

b1 = [0, a[:1][0]]
a2 = a[1:]

b2 = list()
for i in range(0, n - 1):
    b2.append([i + 1, a2[i]])

b2 = sorted(b2, key=itemgetter(1), reverse=True)
b = [b1] + b2

c = 1
ai = 0
print(n - 1)
for el in b:
    ai += 1
    for i in range(0, el[1]):
        print(el[0] + 1, ' ', b[c][0] + 1)
        c += 1
        if c == n:
            return

