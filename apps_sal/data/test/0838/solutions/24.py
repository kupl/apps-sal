n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

s = 0

for l in a:
    k = sum(l)
    s += 2**k - 1
    s += 2**(m-k) - 1

for i in range(m):
    k = sum(l[i] for l in a)
    s += 2**k - 1 - k
    s += 2**(n-k) - 1 - (n-k)

print(s)
