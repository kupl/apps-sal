n = int(input())
s = list(input())
if s[:n // 2] == s[n // 2:]:
    print('Yes')
else:
    print('No')
