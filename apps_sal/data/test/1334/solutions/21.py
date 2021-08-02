n, k = map(int, input().split())
s = input()
L = list(set(s))
L.sort()
if k <= n:
    ans = s[:k]
    if ans == L[-1] * k:
        ans = L[0] * (k + 1)
    else:
        pos = k - 1
        while s[pos] == L[-1]:
            pos -= 1
        i = 0
        while L[i] != s[pos]:
            i += 1
        i += 1
        ans = s[:pos] + L[i]
        l = len(ans)
        ans += L[0] * (k - l)
else:
    ans = s + (k - n) * L[0]

print(ans)
