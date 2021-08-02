from collections import defaultdict as dd, deque

D = dd(list)

n, k = list(map(int, input().split()))
s = input() + '$'

last = None
l = 0
for c in s:
    if last != c:
        if l > 0:
            D[last].append(l)
            l = 0
    last = c
    l += 1

print(max(sum(x // k for x in D[d]) for d in D))
