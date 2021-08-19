from collections import defaultdict
import sys


def update(i, val):
    while i < maxi:
        bit[i] += val
        i += i & (-i)


def query(i):
    ans = 0
    while i > 0:
        ans += bit[i]
        i -= i & (-i)
    return(ans)


# taking inputs

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
bit = [0 for i in range(n + 30)]
maxi = n + 20
one_to_i = []
d = defaultdict(int)
for i in range(n - 1):
    d[l[i]] += 1
    one_to_i.append(d[l[i]])
one_to_i = one_to_i[::-1]
j_to_n = []
d2 = defaultdict(int)
for i in range(n - 1, 0, -1):
    d2[l[i]] += 1
    j_to_n.append(d2[l[i]])
ans = 0
for i in range(n - 1):
    update(j_to_n[i], 1)
    ans += query(one_to_i[i] - 1)
print(ans)
