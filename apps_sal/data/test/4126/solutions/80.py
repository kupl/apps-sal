s = input()
n = len(s)

if s[0:(n - 1) // 2] == s[(n + 3) // 2 - 1:n]:
    print('Yes')
else:
    print('No')
