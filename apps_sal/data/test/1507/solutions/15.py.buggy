n, k = list(map(int, input().split()))
s = input()

a = [None] * n
d = {}

for i in range(n):
    if s[i] not in d:
        a[i] = 1
        d[s[i]] = True

d.clear()
for i in range(n - 1, -1, -1):
    if s[i] not in d:
        if a[i] is None:
            a[i] = 0
        else:
            a[i] = -1
        d[s[i]] = True
c = 0
for el in a:
    if el is not None and el == 1:
        c += 1
    if el is not None and el == 0:
        c -= 1
    if el is not None and el == -1:
        if c + 1 > k:
            print('YES')
            return
    if c > k:
        print('YES')
        return
print('NO')
