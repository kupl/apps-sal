from itertools import accumulate

def z_algorithm(s):
    n = len(s)
    l, d = 1, 0
    ans = [0] * n
    ans[0] = n
    while l < n:
        while l + d < n and s[d] == s[l + d]:
            d += 1
        ans[l] = d
        if d == 0:
            l += 1
            continue
        k = 1
        while l + k < n and k + ans[k] < d:
            ans[l + k] = ans[k]
            k += 1
        l += k
        d -= k
    return ans

z = z_algorithm(input())
n = len(z)
ct = [0] * (n + 1)
match = [False] * (n + 1)
for i, v in enumerate(z):
    ct[v] += 1
    match[n - i] = (n - i) == v
for i in range(n - 1, -1, -1):
    ct[i] += ct[i + 1]
buf = []
for i, v in enumerate(ct):
    if i > 0 and v > 0 and match[i]:
        buf.append('{} {}'.format(i, v))
print(len(buf))
print('\n'.join(buf))

