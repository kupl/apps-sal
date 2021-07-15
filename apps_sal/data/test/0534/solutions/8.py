import sys
n, m = list(map(int, input().split()))
s = list(input())
for i in range(m):
    a = []
    for j in range(n-1):
        if s[j] == 'B' and s[j+1] == 'G': a.append(j)
    for x in a:
        s[x], s[x+1] = 'G', 'B'

for c in s:
    sys.stdout.write(c)
sys.stdout.write('\n')


