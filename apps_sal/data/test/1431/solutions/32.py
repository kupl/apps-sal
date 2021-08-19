import sys
n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]
for i in range(n, 0, -1):
    val = 0
    for j in range(i, n + 1, i):
        val += b[j - 1]
    if val % 2 != a[i - 1]:
        b[i - 1] += 1
num = sum(b)
if num == 0:
    print(0)
else:
    print(num)
    for i in range(n):
        if b[i] != 0:
            print(i + 1)
