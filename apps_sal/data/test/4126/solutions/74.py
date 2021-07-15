s = input()
n = len(s)
l1 = int((n-1)/2)
l2 = int((n+3)/2)
if s == s[::-1] and s[:l1] == s[l2-1:n] :   
    print('Yes')
else :
    print('No')
