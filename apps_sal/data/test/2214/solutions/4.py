import itertools

n, m = list(map(int, input().split()))

rows = []

for _ in range(n):
    rows.append(list(map(int, input())))

#if m < n:
#    rows = [list(rows[i][j] for i in range(n)) for j in range(m)]

# width m
# height n
# n <= m

if m >= 4 and n>=4:
    print(-1)
    return
    
if m==1 or n==1:
    print(0)
    return
    
if n==2 or m==2:
    if n==2:    
        pars = [(rows[0][i]+rows[1][i])%2 for i in range(m)]
    else:
        pars = [(rows[i][0]+rows[i][1])%2 for i in range(n)]
    best = 10**8
    for to_match in [itertools.cycle([0, 1]), itertools.cycle([1, 0])]:
        cost = 0
        for x, y in zip(pars, to_match):
            cost += abs(x-y)
        best = min(best, cost)
    print(best)
    return
    
# n = 3

best = 10**8
if n==3:
    vals = [((rows[0][i]+rows[1][i])%2, (rows[1][i]+rows[2][i])%2) for i in range(m)]
else:
    vals = [((rows[i][0]+rows[i][1])%2, (rows[i][1]+rows[i][2])%2) for i in range(n)]
for up, down in itertools.product([0, 1], repeat=2):
    cost = 0

    for cur_up, cur_down in vals:
        up = 1-up
        down = 1-down
        diff = abs(cur_up-up)+abs(cur_down-down)
        if diff == 2:
            diff = 1
        cost += diff
        
    best = min(best, cost)
print(best)
        

