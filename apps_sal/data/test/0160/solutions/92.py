def get_divisors(x):
    i = 1
    ret = set()
    while i * i <= x:
        if x % i == 0:
            ret.add(i)
            ret.add(x // i)

        i += 1

    return ret


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

sm = sum(a)
divs = get_divisors(sm)

ans = 0
for div in divs:
    mods = [e % div for e in a]
    mods.sort()
    p = 0
    m = n * div - sum(mods)
    for mod in mods:
        p += mod
        m -= div - mod
        if p == m:
            if p <= k:
                ans = max(ans, div)
            break

print(ans)

