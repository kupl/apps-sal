n, k = map(int, input().split())
D = set(map(int, input().split()))
from itertools import count
for ans in count(n,1):
    for c in str(ans):
        if int(c) in D:
            break
    else:
        print(ans)
        break
