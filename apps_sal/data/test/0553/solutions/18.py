n=int(input())
l=[input() for i in range(n)]
print(min([sum(1 for k in range(6) if l[i][k]!=l[j][k])-1 for i in range(n) for j in range(i+1,n)]+[12])//2)
