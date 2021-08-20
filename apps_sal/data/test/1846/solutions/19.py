from sys import stdin
input = stdin.readline
file = open('input.txt', 'r')
num = file.readlines()
file.close()
n = int(num[0])
arr = [int(x) for x in num[1].split()]
f = [0] * (n + 1)
b = [0] * (n + 1)
ans = 1e+18
for i in range(1, n + 1):
    if arr[i - 1] >= 0:
        f[i] = f[i - 1] + 1
    else:
        f[i] = f[i - 1]
f.pop(0)
for i in range(n - 1, -1, -1):
    if arr[i] <= 0:
        b[i] = b[i + 1] + 1
    else:
        b[i] = b[i + 1]
for i in range(n - 1):
    ans = min(ans, f[i] + b[i + 1])
with open('output.txt', 'a') as file:
    file.write('%d\n' % ans)
