n=int(input())
l=[input() for i in range(n)]
print(min([sum(a!=b for a,b in zip(l[i],l[j]))-1 for i in range(n) for j in range(i+1,n)]+[12])//2)
