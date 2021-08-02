from collections import defaultdict as dd
N = int(input())
A = [int(x) for x in input().split()]

Dict = dd(lambda: 0)
for a in A:
    Dict[a] += 1

if N & 1:
    Dict[0] += 1
f = (lambda: (lambda x: 0 if x & 1 else 2) if N & 1 else (lambda x: 2 if x & 1 else 0))()
Possible = {i: f(i) for i in range(N)}
for key, value in list(Dict.items()):
    if value != Possible[key]:
        print((0))
        return
else:
    print((2**(N // 2) % 1000000007))
