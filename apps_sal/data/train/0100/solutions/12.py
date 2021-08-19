# https://codeforces.com/contest/1263/problem/A

t = int(input())
for i in range(t):
    rgb = list(map(int, input().split()))
    rgb.sort()
    ans = min(sum(rgb) // 2, sum(rgb[:2]))
    print(ans)
