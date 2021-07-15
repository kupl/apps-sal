import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

k = int(read())
n = 50
a = [n - 1] * n
x, y = divmod(k, n)
for i in range(n):
    a[i] += x - y
    if i < y:
        a[i] += n + 1
print(n)
print((*a))

