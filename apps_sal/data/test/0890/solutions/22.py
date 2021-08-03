n, l, r, x = [int(y) for y in input().split()]
c = [int(y) for y in input().split()]
c.sort()
ans = [0]


def solve(ans, tasklist=[], e=0):
    if sum(tasklist) <= r and sum(tasklist) >= l and len(tasklist) >= 2 and max(tasklist) - min(tasklist) >= x:
        ans[0] += 1
    for i in range(e, n):
        tasklist.append(c[i])
        solve(ans, tasklist, i + 1)
        del tasklist[len(tasklist) - 1]


solve(ans)
print(ans[0])
