def ssum(s):
    return sum(map(int, list(s)))
for _ in range(int(input())):
    n, s = list(map(int, input().split()))
    ns = str(n)
    if ssum(ns) <= s:
        print(0)
        continue

    ans = float("inf")
    for i in range(0, len(ns)):
        x = 1
        if i > 0:
            x = int(ns[:i])+1
        acc = 0
        while x > 0:
            acc += x % 10
            x //= 10
        if acc > s:
            continue
        y = 10**(len(ns)-i) - int(ns[i:])
        ans = min(ans, y)
    print(ans)

