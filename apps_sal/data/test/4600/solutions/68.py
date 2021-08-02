n, m = map(int, input().split())
ans = [0, 0]
ac = [0 for _ in range(n)]
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if ac[p] == -1:
        continue
    elif s == "AC":
        ans[0] += 1
        ans[1] += ac[p]
        ac[p] = -1
    else:
        ac[p] += 1
print(*ans)
