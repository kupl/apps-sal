from collections import defaultdict as dd, deque

H = dd(int)

s = input()

for c in s:
    H[c] += 1

if len(H) == 4 or (len(H) == 3 and max(H.values()) > 1) or (len(H) == 2 and min(H.values()) > 1):
    print('Yes')
else:
    print('No')
