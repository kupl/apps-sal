n,h=list(map(int,input().split()))
print(sum(1 if x<=h else 2 for x in map(int,input().split())))

