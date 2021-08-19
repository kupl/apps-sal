n, m = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

b = []  # subsums
curr = 0

for i in a:
    curr += i
    b.append(curr)


k = []
for i in range(min(m, n)):
    k.append(b[i])
    print(b[i], end=' ')

for i in range(min(m, n), n):
    k[i % m] += b[i]
    print(k[i % m], end=' ')
