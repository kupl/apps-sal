def isPal(s):
    s = str(s)
    n = len(s)
    f = 1
    for i in range(n // 2):
        f &= s[i] == s[n - i - 1]
    return f


(a, b) = list(map(int, input().split()))
ans = 0
for i in range(a, b + 1):
    if isPal(i):
        ans += 1
print(ans)
