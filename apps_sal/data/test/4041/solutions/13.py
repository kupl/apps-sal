def pp(s, t):
    last = 0
    for i in t:
        if last == len(s):
            return 0
        while(s[last] != i):
            last += 1
            if last == len(s):
                return 0
        last += 1
    return 1

s, t = input(), input()
ans = 0
n = len(s)
for i in range(n):
    for j in range(i, n):
        if pp(s[:i] + s[(j + 1):], t):
            ans = max(ans, j - i + 1)
print(ans)


# print(pp('bbaba', 'bb'))

# s = '0123456789'
# print(s[:2] + s[4:])

