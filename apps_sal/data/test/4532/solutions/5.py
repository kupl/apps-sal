t = int(input())
from collections import Counter

for case in range(t):
    n, k = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    w = Counter(x % k for x in a)
    v = 0
    for x, freq in list(w.items()):
        if x == 0: continue
        if freq == 0: continue
        
        r = (-x) % k
        v = max(v, r + (freq-1)*k+1)

    print(v)

