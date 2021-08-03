import sys
from collections import Counter


def i_ints():
    return list(map(int, sys.stdin.readline().split()))


n, m = i_ints()
a = list(i_ints())

r = [x % m for x in a]
c = Counter(r)
c = [c[i] for i in range(m)]

rem2ind = [[] for i in range(m)]
for i, x in enumerate(r):
    rem2ind[x].append(i)


R = n // m

for i, inds in enumerate(rem2ind):
    if len(inds) > R:
        next_big = i
        break
else:
    next_big = m
next_small = next_big + 1
# for i in range(next_big + 1, next_big + m):
#    if len(rem2ind[i%m]) < R:
#        next_small = i
#        break

moves = 0
while next_big < m:
    next_small = max(next_small, next_big + 1)
    num = max(c[next_big] - R, 0)
    while num > 0:
        num2 = max(R - c[next_small % m], 0)
        delta = min(num, num2)
        num -= delta
        c[next_small % m] += delta
        step = next_small - next_big
        for i in rem2ind[next_big][num:num + delta]:
            a[i] += step
        moves += delta * step
        if c[next_small % m] >= R:
            next_small += 1
#        print(next_big, next_small, delta, step, moves)
    next_big += 1

print(moves)
print(" ".join(map(str, a)))


# def distribute(k, i):
#    """ distribute i elements from position k to the following positions, not exceeding R"""
#    while i > 0:
#        c[k] -= i
#        moves[k] += i
#        k = (k+1) % m
#        c[k] += i
#        i = max(0, c[k] - R)
#
#moves = [0] * m
#
# for k in range(m):
#    if c[k] > R:
#        distribute(k, c[k] - R)
#
# print(sum(moves))
#
# for k, x in enumerate(a):
#    while moves[x%m]:
#        moves[x%m] -= 1
#        x += 1
#    a[k] = x
#
#print( " ".join(map(str, a)))
