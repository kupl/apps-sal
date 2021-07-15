s = input()
n = len(s)
a = len(s) // 4
if s[:n // 2] == s[n // 2 + 1:]:
    print('Yes')
        
else:
    print('No')

