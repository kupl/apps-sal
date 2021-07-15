n,s=open(0);j=r=0
for i in range(int(n)):
    while (j<int(n))and(s[i:j] in s[j:]):j+=1
    r=max(r,j-i-1)
print(r)
