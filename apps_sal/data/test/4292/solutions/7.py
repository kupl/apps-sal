N,K=map(int,input().split())
poe=list(map(int,input().split()))
poe=sorted(poe)

print(sum(poe[:K]))
