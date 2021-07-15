import sys
s=input().split('+')

s.sort()

n=len(s)

for i in range(n-1):
    print(s[i],end='+')
print(s[n-1])
    
    


