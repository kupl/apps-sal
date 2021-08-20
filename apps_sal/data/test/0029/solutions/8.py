def comp(n, m):
    rtn = 0
    for i in range(6):
        if n[i] != m[i]:
            rtn += 1
    return rtn


n = list(map(int, list(input())))
ans = 6
for i in range(1000000):
    m = []
    for _ in range(6):
        m.append(i % 10)
        i //= 10
    m = list(reversed(m))
    if sum(m[:3]) == sum(m[3:]):
        ans = min(ans, comp(n, m))
print(ans)
