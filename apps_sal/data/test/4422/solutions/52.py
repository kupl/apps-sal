n,k=map(int, input().split())
s=list(input())

ss=s[k-1]
p=ss.lower()
#print(p)
s[k-1]=p
#print(s[k-1])
#print(s)

ans="".join(s)
print(ans)
