import sys
input = sys.stdin.readline
print = sys.stdout.write
n, k, q = map(int, input().split())
ar = [0] * (200000 + 2)


def f(l, r):
    ar[l] += 1
    ar[r + 1] -= 1


for x in range(n):
    a, b = map(int, input().split())
    f(a, b)
for x in range(1, 200000 + 1):
    ar[x] += ar[x - 1]
for x in range(1, 200000 + 1):
    ar[x] = ar[x] >= k
for x in range(1, 200000 + 1):
    ar[x] += ar[x - 1]
for el in range(q):
    a, b = map(int, input().split())
    print(str((ar[b] - ar[a - 1])) + "\n")
