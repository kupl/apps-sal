import sys

n = int(input())
h = list(map(int, input().split()))
maxh = h[0]
for i in range(len(h)):
    if maxh > h[i] + 1:
        print('No')
        return
    else:
        maxh = max(maxh, h[i])
print('Yes')
