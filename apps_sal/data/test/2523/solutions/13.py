s=input();l=[];n=len(s)
for i in range(n-1):
 if s[i]!=s[i+1]:l+=[max(i+1,n-i-1)]
print(min(l)if l else n)
