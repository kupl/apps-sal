n = int(input())  # request number
x = []  # requests array
for i in range(n):  # input requests array
    c, p = map(int, input().split())
    x += [(p, c, i)]  # please note: p is value
k = int(input())  # table number
r = list(map(int, input().split()))  # tables array
s = 0  # sum
q = []  # results array
for (v, c, a) in reversed(sorted(x)):  # v=value c=cost
    p = -1
    u = 100000
    for (j, z) in enumerate(r):  # j=index, z=value
        if c <= z < u:  # request size <= table index < cur index
            p = j
            u = z
    if p > -1:
        r[p] = 0   # make table size=0 indicates it has been used.
        q += [(a, p)]
        s += v
print(len(q), s)
for (i, j) in q:
    print(i + 1, j + 1)
