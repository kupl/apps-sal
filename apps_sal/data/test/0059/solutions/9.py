n = int(input())
a = list(map(int, input().split()))
s = input()
d = []
cl = 0
mi = 0
i = 0
while i < len(s):
    while i < len(s) and s[i] == '1':
        i += 1
        cl += 1
    while i < len(s) and s[i] == '0':
        i += 1
    d.append([mi, cl])
    cl = 0
    mi = i
d.append([n - 1, 1])
if s[-1] != '1':
    d.append([n - 1, 0])
z = []
for i in range(len(d) - 1):
    z += sorted(a[d[i][0]:d[i][1] + d[i][0] + 1])
    z += a[d[i][1] + d[i][0] + 1:d[i + 1][0]]
print('YES' if z == list(range(1, n + 1)) else 'NO')
