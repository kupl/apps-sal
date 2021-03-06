M = 9999999999879998


def str_hash(s):
    h = 0
    p = 1
    for c in s:
        h = (h + p * ord(c)) % M
        p = p * 197 % M
    return h


(n, m) = [int(i) for i in input().split()]
a = set()
for i in range(n):
    s = input()
    h = str_hash(s)
    p = 1
    for j in range(len(s)):
        for k in range(97, 100):
            if ord(s[j]) != k:
                a.add((h + p * (k - ord(s[j]))) % M)
        p = p * 197 % M
ans = []
for i in range(m):
    s = input()
    b = str_hash(s)
    if b in a:
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))
