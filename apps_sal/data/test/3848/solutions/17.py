def trans(c):
    return chr(ord(c) + 1)


(n, p) = list(map(int, input().split()))
s = list(input())
s[n - 1] = trans(s[n - 1])
i = n - 1
while i >= 0 and i < n:
    if ord(s[i]) >= ord('a') + p:
        s[i] = 'a'
        i -= 1
        s[i] = trans(s[i])
    elif i > 0 and s[i] == s[i - 1] or (i > 1 and s[i] == s[i - 2]):
        s[i] = trans(s[i])
    else:
        i += 1
else:
    print('NO' if i < 0 else ''.join(s))
