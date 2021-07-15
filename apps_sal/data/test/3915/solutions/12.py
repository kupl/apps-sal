n=2 * 10 ** 6 + 10 ** 5
p,q=list(map(int,input().split(" ")))
pi=0
si=0
pr=[0]*n
pr[1]=1
for i in range(2,n):
    if pr[i]==0:
        for j in range(i*i,n,i):
            pr[j]=1

res='Palindromic tree is better than splay tree'
for i in range(1,n):
    if pr[i]==0:
        pi+=1
    j=str(i)
    if j==j[::-1]:
        si+=1
    if q*pi<=si*p:
        res=i
print(res)

