def isSubSequence(str1,str2,m,n): 
    j = 0 
    i = 0 
    while j<m and i<n: 
        if str1[j] == str2[i]:     
            j = j+1    
        i = i + 1
    return j==m
s=input()
t=input()
LengthT=len(t)
A=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        p=s[:i]+s[j:]
        if isSubSequence(t,p,LengthT,len(p)):
            A.append(j-i)
try:
    print(max(A))
except:
    print(0)
