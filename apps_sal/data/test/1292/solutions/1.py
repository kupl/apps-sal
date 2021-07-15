from collections import defaultdict as dd, deque

n,m,p = list(map(int,input().split()))
S = [0]+[int(x) for x in input().split()]
M = [list(input())+['#'] for i in range(n)]
M.append(['#']*m)

front = [[], [],[],[],[],[],[],[],[],[]]

for i in range(n):
    for j in range(m):
        if M[i][j] not in '.#':
            a = int(M[i][j])
            front[a].append((i,j))
            M[i][j] = a

def expand(p):
    s = S[p]
    Q = deque()
    for i,j in front[p]:
        Q.append((i,j,0))

    new = False
    nfront = []
    while Q:
        i,j,d = Q.popleft()
        nfront.append((i,j))
        if d >= s:
            continue

        for di,dj in [(-1,0), (1,0), (0,1), (0,-1)]:
            if M[i+di][j+dj] == '.':
                new = True
                M[i+di][j+dj] = p
                Q.append((i+di,j+dj,d+1))

    nnfront = []
    for i,j in nfront:
        if M[i-1][j] == '.' or \
           M[i+1][j] == '.' or \
           M[i][j+1] == '.' or \
           M[i][j-1] == '.':
            nnfront.append((i,j))

    front[p] = nnfront
    return new


while any([expand(i) for i in range(1,p+1)]):
    #for _ in M:
    #    print(*_)
    pass

C = dd(int)
for i in range(n):
    for j in range(m):
        C[M[i][j]] += 1
print(*(C[i] for i in range(1,p+1)))

