def checkLeft(s):
    c1, c2 = 0, 0
    f = 1
    for i in s:
        if i == '(':
            c1 += 1
        else:
            c2 += 1
        if c2 > c1:
            f = 0
            break
    return f


def checkRight(s):
    c1, c2 = 0, 0
    f = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            c1 += 1
        else:
            c2 += 1
        if c1 > c2:
            f = 0
            break
    return f


n = int(input())
N = 6 * (10**5) + 1
b = [0] * N
for i in range(n):
    s = input()
    c1, c2 = 0, 0
    for j in s:
        if j == '(':
            c1 += 1
        else:
            c2 += 1
    if (c1 > c2 and checkLeft(s)) or (c1 < c2 and checkRight(s)) or (c1 == c2 and checkLeft(s) and checkRight(s)):
        b[c1 - c2 + N // 2] += 1

ans = 0
for i in range(-N // 2, 1):
    if b[i + N // 2] > 0 and b[-i + N // 2] > 0:
        ans += b[i + N // 2] * b[-i + N // 2]
print(ans)
