from collections import defaultdict
import sys
input = sys.stdin.readline
def case():
    n = int(input())
    s = input().strip()
    t = 1
    x, y = 0, 0
    d = defaultdict(list)
    d[(0, 0)].append(0)
    anslen = 10**10
    ans = []
    for i in s:
        if i == 'L':
            x-=1
        elif i == 'R':
            x+=1
        elif i == 'D':
            y-=1
        elif i == 'U':
            y+=1
        if d[(x, y)] != []:
            if t-d[(x, y)][-1] < anslen:
                anslen = t-d[(x, y)][-1]
                ans = [d[(x, y)][-1], t]
        d[(x, y)].append(t)
        t+=1
    if anslen == 10**10:
        print(-1)
    else:
        print(ans[0]+1, ans[1])
for _ in range(int(input())):
    case()
