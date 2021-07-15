n,k=map(int,input().split())
s=list(input())
s[k-1]=str.lower(s[k-1])
print(''.join(s))
