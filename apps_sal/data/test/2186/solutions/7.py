(n, m) = list(map(int, input().split()))
mod = 9999999999999983
v = set()
for i in range(n):
    s = input()
    l = len(s)
    pow = 1
    h = 0
    for i in range(l):
        h = (h + ord(s[i]) * pow) % mod
        pow = pow * 203 % mod
    pow = 1
    for i in range(l):
        for j in range(97, 100):
            if ord(s[i]) != j:
                v.add((h + (j - ord(s[i])) * pow) % mod)
        pow = pow * 203 % mod
ans = []
for i in range(m):
    s = input()
    pow = 1
    h = 0
    for i in range(len(s)):
        h = (h + ord(s[i]) * pow) % mod
        pow = pow * 203 % mod
    ans.append('YES' if h in v else 'NO')
print('\n'.join(ans))
