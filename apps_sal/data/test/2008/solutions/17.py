
N_ = 100010

n = int(input())
a = []
b = []
d = []
sum = 0
for i in range(n):
    ai, bi = list(map(int, input().split()))
    a.append(ai)
    b.append(bi)
    d.append(ai - bi)
    sum += bi * n - ai
d.sort()
d = d[::-1]
for i in range(n):
    sum += d[i] * (i + 1)

print(sum)
