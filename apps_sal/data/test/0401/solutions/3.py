import sys
(n, n1) = map(int, input().split())
a1 = set(map(int, input().split()))
a2 = set(map(int, input().split()))
a = set(a1).intersection(a2)
if a:
    print(sorted(list(a))[0])
else:
    a = sorted(list(a1))[0]
    b = sorted(list(a2))[0]
    (a, b) = (min(a, b), max(a, b))
    print(a, b, sep='')
