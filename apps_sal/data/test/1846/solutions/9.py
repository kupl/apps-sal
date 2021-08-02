import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
l = list(map(int, input().split()))
a = [0 for i in range(n)]
b = [0 for i in range(n)]
if l[0] >= 0:
    a[0] = 1
for i in range(1, n):
    if l[i] >= 0:
        a[i] = a[i - 1] + 1
    else:
        a[i] = a[i - 1]

for i in range(n - 2, -1, -1):
    if l[i + 1] <= 0:
        b[i] = b[i + 1] + 1
    else:
        b[i] = b[i + 1]

ans = n
for i in range(n - 1):
    ans = min(ans, a[i] + b[i])
print(ans)
