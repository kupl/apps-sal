from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
a = [int(j) for j in input().split()]
c = Counter(a)
l = c.most_common()
ll = []
for i, j in l:
    ll.append(j)
ll.sort()
s = sum(ll)
rem = 0
for k in range(1, n + 1):
    rest = k - rem
    while ll and ll[-1] > s // rest:
        s -= ll[-1]
        ll.pop()
        rem += 1
        rest -= 1
    print((s // rest))
