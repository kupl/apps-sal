n = int(input())
res = set()

def solve(p, l):
    if p > n or l > 10:
        return
    if p > 0:
        res.add(p)
    solve(p * 10 + a, l + 1)
    solve(p * 10 + b, l + 1)

for a in range(0, 10):
    for b in range(0, a):
        solve(0, 0)
print(len(res))

