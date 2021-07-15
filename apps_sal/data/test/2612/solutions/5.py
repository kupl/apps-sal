import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve():
    n = int(input())
    s = list(map(int, input().split()))
    ans = [0]*n
    for i in range(1, n+1):
        ans[i-1] = max(ans[i-1], 1)
        for j in range(2*i, n+1, i):
            if s[i-1] < s[j-1]:
                ans[j-1] = max(ans[j-1], ans[i-1]+1)
    print(max(ans))

t = int(input())
for i in range(t):
    solve()


