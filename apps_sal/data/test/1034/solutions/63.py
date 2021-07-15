x,y,z,k=map(int,input().split())
a=sorted(list(map(int,input().split())),reverse=True)
b=sorted(list(map(int,input().split())),reverse=True)
c=sorted(list(map(int,input().split())),reverse=True)

ab=[i+j for j in b for i in a]
ab.sort(reverse=True)
abc=[i+j for j in c[:k] for i in ab[:k]]
abc.sort(reverse=True)

print(*abc[:k],sep='\n')

