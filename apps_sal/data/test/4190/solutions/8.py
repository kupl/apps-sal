import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

num = [0 for i in range(n)]
for cur in b:
    num[cur] += 1

next = list(range(+1, n + 1))
next[n - 1] = 0

res = []
for i in range(n):
    value = (n - a[i]) % n
    while num[value] == 0:
        if num[next[value]] == 0:
            next[value] = next[next[value]]
        value = next[value]
    res.append((a[i] + value) % n)
    num[value] -= 1

print(' '.join(map(str, res)))
