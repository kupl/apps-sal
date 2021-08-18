n = int(input())
s = [int(x) for x in input().split()]
d = {}

for i in range(n):
    q = s[i]
    t2 = 0
    while q % 2 == 0:
        q //= 2
        t2 += 1
    q = s[i]
    t3 = 0
    while q % 3 == 0:
        q //= 3
        t3 += 1
    d[(t3, -t2)] = s[i]

w = [i for i in d]
w.sort(reverse=1)
for i in range(n):
    print(d[w[i]], end=' ')
