
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n, m = list(map(int, input().split()))

a = []
b = []

for i in range(n):
    s = input().strip()
    for j in range(m):
        if s[j] == 'B':
            a.append(i)
            b.append(j)

a.sort()
b.sort()
print((a[0] + a[-1]) // 2 + 1, (b[0] + b[-1]) // 2 + 1)
