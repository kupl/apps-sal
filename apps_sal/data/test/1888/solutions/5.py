n,m = list(map(int,input().split()))
xs = [0]*n
for _ in range(m):
    a,b,c = list(map(int,input().strip().split()))
    xs[a-1] -= c
    xs[b-1] += c
print(sum(x for x in xs if x>0))

