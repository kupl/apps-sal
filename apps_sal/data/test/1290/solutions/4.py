from collections import defaultdict as dd, deque

n,m = list(map(int,input().split()))
H = [0]*n

for c in map(int,input().split()):
    H[c-1] += 1

print(min(H))

