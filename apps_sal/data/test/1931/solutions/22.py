import sys
T = int(sys.stdin.readline().strip())
cache = [2]
L = 1
for t in range(T):
    n = int(sys.stdin.readline().strip())
    while cache[-1] < n:
        L += 1
        cache.append(L * (L + 1) + L * (L - 1) // 2)
    l = 0
    r = L
    while l < r - 1:
        m = (l + r) // 2
        if cache[m] <= n and (m + 1 == L or cache[m + 1] > n):
            l = m
            break
        if cache[m] < n:
            l = m
        else:
            r = m
    cnt = 0
    while l >= 0 and n > 1:
        if n >= cache[l]:
            n -= cache[l]
            cnt += 1
        else:
            l -= 1
    print(cnt)
