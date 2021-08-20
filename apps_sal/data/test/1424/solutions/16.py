(n, m, k) = map(int, input().split())
s = 0
a = []
for i in range(m + 1):
    a.append(int(input()))
p = a[m]
for i in range(m):
    d = list(map(int, list(bin(a[i] ^ p)[2:])))
    if sum(d) <= k:
        s += 1
print(s)
