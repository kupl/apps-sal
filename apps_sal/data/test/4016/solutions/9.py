s=input().split()
n=int(s[0])
k=int(s[1])
s=input()
if n==1:
    print(s*k)
elif k==1:
    print(s)
else:
    flag=True
    for i in range(1,n):
        if s[:-i]==s[i:]:
            print(s+s[-i:]*(k-1))
            flag=False
            break
    if flag:
        print(s*k)

