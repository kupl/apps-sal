n=int(input())
l=sorted(list(map(int,input().split())))
print("Yes" if l[-1]<sum(l[:-1]) else "No")
