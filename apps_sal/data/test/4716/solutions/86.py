a,b=list(map(int,input().split()))
N = sorted(list(map(int,input().split())))[::-1]
print((sum(N[:b])))

