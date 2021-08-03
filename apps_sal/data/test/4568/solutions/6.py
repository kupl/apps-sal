n = int(input())
s = input()


def check(a, b):
    c = [0] * 26
    d = [0] * 26
    for i in range(len(a)):
        c[ord(a[i]) - 97] = 1
    for i in range(len(b)):
        d[ord(b[i]) - 97] = 1
    ans = 0
    for i in range(26):
        if c[i] == 1 and d[i] == 1:
            ans += 1
    return ans


res = 0
for i in range(n):
    res = max(res, check(s[:i], s[i:]))
print(res)
