n = int(input())
s = input()
r = 0
g = 0
b = 0
for i in s:
    if i == 'R':
        r += 1
    elif i == 'G':
        g += 1
    else:
        b += 1
ans = r * g * b

for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            continue
        k = 2 * j - i
        if k >= n or s[k] == s[i] or s[k] == s[j]:
            continue
        ans -= 1

print(ans)
