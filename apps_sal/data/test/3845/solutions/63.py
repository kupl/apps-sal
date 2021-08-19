# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

a, b = list(map(int, readline().split()))
h = w = 100
res = [[0] * w for _ in range(50)] + [[1] * w for _ in range(50)]
a -= 1
b -= 1

q = a // 50
r = a % 50
for i in range(q):
    res[2 * i][::2] = [1] * 50
res[2 * q][:2 * r:2] = [1] * r

q = b // 50
r = b % 50
for i in range(q):
    res[2 * i + 51][::2] = [0] * 50
res[2 * q + 51][:2 * r:2] = [0] * r

# 0: 黒: #
print((h, w))
for ri in res:
    print(("".join("#" if rij == 0 else "." for rij in ri)))
