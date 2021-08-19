(n, p) = map(int, input().split())
s = list(map(ord, input()))
i = n - 1
s[i] += 1
p += 97
while ~i and i < n:
    if s[i] == p:
        s[i] = 97
        i -= 1
        s[i] += 1
    elif i and s[i] == s[i - 1]:
        s[i] += 1
    elif i > 1 and s[i] == s[i - 2]:
        s[i] += 1
    else:
        i += 1
if i < 0:
    print('NO')
else:
    for i in s:
        print(chr(i), end='')
