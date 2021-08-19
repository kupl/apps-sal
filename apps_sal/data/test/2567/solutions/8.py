import sys
sys.setrecursionlimit(10000)
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = ''
    for i in range(n):
        ans += s[n - 1]
    print(ans)
