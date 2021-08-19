def solve(a):
    check2 = [x + y for (x, y) in zip(a[0], a[-1])]
    if any(check2):
        return 2
    checkn = [sum(l) for l in zip(*a)]
    if any(check2) and any(checkn):
        return 3
    return 4


(n, m) = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print(min(solve(a), solve(list(zip(*a)))))
