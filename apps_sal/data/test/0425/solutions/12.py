n, p = list(map(int, input().split()))
ans = -1
l = 1
while n - l * p > 0:
    if p == 0:
        s = bin(n)[2:]
        for i in range(len(s)):
            if s[i] == '1':
                ans += 1
        ans += 1
        break
    k = n - l * p
    v1, v2 = 0, 0
    s = bin(k)[2:]
    for i in range(len(s)):
        if s[i] == '1':
            v1 += 1
            v2 += 1
        if i > 0 and s[i - 1] == '1' and s[i] == '0':
            v2 += 1
            s = s[:i] + '1' + s[i + 1:]
    if v1 <= l <= v2:
        ans = l
        break
    l += 1
print(ans)

