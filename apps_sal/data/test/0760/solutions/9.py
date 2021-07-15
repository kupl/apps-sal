def tandemRepeat(i,j):
    a=s[i:i+j-1]
    b=s[i-j:i-1]
    for k in range(len(a)):
        if a[k]==b[k] or a[k]=='*' or b[k]=='*':
            continue
        else:
            return False
    return True

s=input()
n=int(input())
s=s+("*"*n)
#print(s)
ans=-1
for i in range(len(s)):
    for j in range(1,len(s)):
        if i+j-1<len(s) and i-j>=0 and tandemRepeat(i,j):
            if ans<j : ans=j
print(ans*2)
            

