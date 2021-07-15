from itertools import accumulate
N,C = map(int,input().split())
xs = []
vs = []
for _ in range(N):
    x,v = map(int,input().split())
    xs.append(x)
    vs.append(v)
vacc = [0]+list(accumulate(vs, lambda x,y:x+y))
lacc = [0]+[vacc[i+1]-xs[i] for i in range(N)]
racc = [vacc[-1]-vacc[i]-C+xs[i] for i in range(N)]+[0]
for i in range(1, N):
    lacc[i] = max(lacc[i], lacc[i-1])
racc[-1] = (racc[-1], 0)
for i in range(N, 0, -1):
    if racc[i-1] > racc[i][0]:
        racc[i-1] = (racc[i-1], C-xs[i-1])
    else:
        racc[i-1] = racc[i]
xs = [0]+xs
ans = 0
for i in range(N+1):
    l = lacc[i]
    r, d = racc[i]
    ans = max(ans, l+r-xs[i], l+r-d, l, r)
print(ans)
