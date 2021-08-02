m = dict()
n = int(input().strip())
m['polycarp'] = 0
for i in range(n):
    n1, n2 = input().rstrip().lower().split(' reposted ', 1)
    m[n1] = m[n2] + 1
print(max(m.values()) + 1)
