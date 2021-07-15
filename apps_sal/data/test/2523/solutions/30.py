import math
def f(s):
    if len(s)%2==0: p=len(s)//2-1
    else: p=len(s)//2
    
    q=p
    while  q<len(s) and s[p]==s[q]:
        q+=1
    return q



s=input()

print(min(f(s),f(s[::-1])))
