def merge(res, s):
    pi = [0 for i in range(len(s) + 1)]
    pi[0] = -1
    b = -1
    for i in range(1, len(s) + 1):
        while b > -1 and s[i - 1] != s[b]:
            b = pi[b]
        b += 1
        pi[i] = b
    b = 0
    for i in range(max(0, len(res) - len(s)), len(res)):
        while b > -1 and res[i] != s[b]:
            b = pi[b]
        b += 1
    for i in range(b, len(s)):
        res.append(s[i])


n = int(input())
s = input().split()
res = [*s[0]]
for i in range(1, n):
    merge(res, s[i])
print(''.join(res))
