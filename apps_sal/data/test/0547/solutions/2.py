from collections import Counter


def f(x, k):
    return 5 * ((x - 1) // k) + x


n, k = [int(s) for s in input().split()]
ctr = Counter()
for i in range(n):
    ctr[len(input())] += 1

lc = len(input())

x = sum(ctr[l] for l in ctr if l < lc) + 1
y = sum(ctr[l] for l in ctr if l <= lc)

print(f(x, k), f(y, k))
