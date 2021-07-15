n=int(input())
l=[input() for i in range(n)]
def d(a,b): return sum(1 for k in range(6) if l[a][k]!=l[b][k])-1
print(min({d(i,j) for i in range(n) for j in range(i+1,n)}|{12})//2)
