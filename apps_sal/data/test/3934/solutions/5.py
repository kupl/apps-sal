from collections import defaultdict

n = int(input())
d = defaultdict(int)


for i in range(n - 1):
    sa = input().split()
    d[sa[0]] += 1
    d[sa[1]] += 1

for v in list(d.values()):
    if v == 2:
        print('NO')
        return

print('YES')
