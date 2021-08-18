
from collections import defaultdict


t = 1

for test in range(t):
    found = 0
    l, r = list(map(int, input().split()))
    for i in range(l, r + 1):
        a = list(str(i))
        if len(set(a)) == len(a):
            print(i)
            found = 1
            break
    if found == 0:
        print(-1)
