import math
t = int(input())
for w in range(t):
    s = sorted(input().split('0'), reverse=True)
    c = 0
    for i in range(0, len(s), 2):
        c += len(s[i])
    print(c)
