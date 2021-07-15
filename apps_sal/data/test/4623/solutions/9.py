from bisect import bisect_left
import sys
input=sys.stdin.readline
t = int(input())

for _ in range(t):
    l = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    ans = 0
    
    for w in range(1,2*l+1):
        c = 0
        used = {}
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] + a[j] == w and i not in used and j not in used:
                    c += 1
                    used[i] = 1
                    used[j] = 1
        ans = max(c, ans)
    print(ans)
