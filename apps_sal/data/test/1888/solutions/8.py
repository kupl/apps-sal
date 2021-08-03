__author__ = 'asmn'
n, m = tuple(map(int, input().split()))
l = [0] * n
for i in range(m):
    a, b, c = tuple(map(int, input().split()))
    l[a - 1] += c
    l[b - 1] -= c

print(sum(abs(x) for x in l) // 2)
