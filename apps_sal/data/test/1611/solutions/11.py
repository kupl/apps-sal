n=int(input())
l=sorted(map(int,input().split()))
print(l[-1]-sum(l[:-1])+1)
