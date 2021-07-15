n = int(input())
s = k = input()
if len(s) < n or len(s) == n and len(set(s)) < n or len(set(s))<n :
    print('NO')
elif len(s) == n:
    print ('YES')
    for i in range(n):
        print(s[i])
        
        
else:
    print('YES')
    r = ''
    for element in s:
        if element not in r:
            r+=element
    
    j = 0
    for i in range(n-1):
        print(s[j:s.find(r[i+1])])
        j = s.find(r[i+1])        
        
        
    print(s[j:])
