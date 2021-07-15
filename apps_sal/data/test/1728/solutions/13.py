n = int(input())
P = [0]+list(map(lambda c:int(c)-1,input().split()))
C = list(map(int,input().split()))

cnt = sum(C[i]==C[p] for i,p in enumerate(P))

print(n-cnt+1)
