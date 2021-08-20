n = int(input())
s = input()
(r, g, b) = (0, 0, 0)
for i in range(n):
    if s[i] == 'R':
        r += 1
    elif s[i] == 'G':
        g += 1
    elif s[i] == 'B':
        b += 1
ans = r * g * b
for i in range(n):
    for j in range(i + 1, n):
        k = j + j - i
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and (s[k] != s[i]):
                ans -= 1
print(ans)
