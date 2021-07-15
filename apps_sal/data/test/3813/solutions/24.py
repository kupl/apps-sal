n = int(input())
p = [0,0] + list(map(int,input().split()))
x = [0] + list(map(int,input().split()))

child = [[] for _ in range(n+1)]
for i,pi in enumerate(p[2:],2):
    child[pi].append(i)

tp = []
stack = [1]
while(stack):
    i = stack.pop()
    tp.append(i)
    for ci in child[i]:
        stack.append(ci)

tp = tp[::-1]

cost = [[-1,-1] for _ in range(n+1)]
for i in tp:
    tot = 0
    mins = 0
    dif = []
    for ci in child[i]:
        a,b = cost[ci]
        if(a > b):
            a,b = b,a
        mins += a
        tot += a+b
        dif.append(b-a)

    if( mins > x[i]):
        print('IMPOSSIBLE')
        return

    dp = 1
    dp_max = (1<<(x[i] - mins+1)) - 1
    for di in dif:
        dp = (dp|(dp<<di))&dp_max

    max_dif = -1
    while(dp>0):
        dp//=2
        max_dif += 1

    a = x[i]
    b = tot - mins - max_dif
    cost[i] = [a,b]

print('POSSIBLE')
