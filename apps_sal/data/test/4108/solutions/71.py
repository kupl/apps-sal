import sys
s = list(input())
t = list(input())
a = [-1 for _ in range(26)]
b = [-1 for _ in range(26)]

for i in range(len(s)):
    num0, num1 = a[ord(s[i])-97], b[ord(t[i])-97]
    if num0 >= 0:
        if chr(num0+97) != t[i]:
            print('No')
            return
    else:
        a[ord(s[i])-97] = ord(t[i])-97
        
    if num1 >= 0:
        if chr(num1+97) != s[i]:
            print('No')
            return
    else:
        b[ord(t[i])-97] = ord(s[i])-97
            
print('Yes')

