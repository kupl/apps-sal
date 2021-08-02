from sys import stdin
n = int(stdin.readline().strip())

s = list(map(int, stdin.readline().strip().split()))
s.sort()
vis = [False for i in range(150100)]
ans = 0
for i in range(n):
    if not vis[s[i] - 1] and (s[i] - 1) != 0:
        vis[s[i] - 1] = True
        ans += 1
    elif not vis[s[i]]:
        ans += 1
        vis[s[i]] = True
    elif not vis[s[i] + 1]:
        ans += 1
        vis[s[i] + 1] = True
print(ans)
