(n, m) = input().split()
n = int(n)
m = int(m)
s = set()
for x in range(n):
    a = input().split()
    for y in a[1:]:
        s.add(int(y))
print('YES' if len(s) == m else 'NO')
