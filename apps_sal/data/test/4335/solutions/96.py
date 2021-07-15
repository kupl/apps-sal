n = int(input())
n1 = n//2
s = input()
s1 = s[n1:]
s2 = s[:n1]
if n % 2 != 0:
    print('No')
else:
    if s1 == s2:
        print('Yes')
    else:
        print('No')
