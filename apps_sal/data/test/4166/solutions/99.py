import sys

n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
sc = [(s - 1, c) for s, c in sc]

ans = ["x"] * n

for s, c in sc:
    if n > 1 and s == 0 and c == 0:
        print(-1)
        return
    elif ans[s] != "x" and ans[s] != c:
        print(-1)
        return
    else:
        ans[s] = c

if n > 1 and ans[0] == "x":
    ans[0] = 1

for i in range(n):
    if ans[i] == "x":
        ans[i] = 0

ans = [str(x) for x in ans]

print("".join(ans))
