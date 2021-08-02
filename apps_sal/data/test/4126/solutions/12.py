s = input()
s1 = s[:len(s) // 2]
s2 = s[:len(s) // 2:-1]
s3 = s[len(s) // 2 + 1:]

if s1 == s2 == s3:
    print('Yes')
else:
    print('No')
