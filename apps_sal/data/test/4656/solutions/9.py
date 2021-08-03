def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    if s[0] * n == s:
        print(n)
        continue
    cnt = {}
    for c in s:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    cnt = [cnt[c] for c in cnt]
    ans = 1
    for x in range(2, n + 1):
        tempK = k % x
        if tempK == 0:
            ans = max(ans, x)
            continue
        mod = x % tempK
        if mod != 0:
            mod = -(mod - tempK)
        times = tempK // gcd(tempK, mod)
        needed = x * times // tempK
        usedBeads = 0
        for num in cnt:
            usedBeads += num - num % needed
        if usedBeads >= x:
            ans = max(ans, x)
    print(ans)
