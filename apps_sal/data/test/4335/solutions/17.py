n = int(input())
s = input()
if n % 2 == 0 and s[n // 2:] * 2 == s:
    print('Yes')
else:
    print('No')
