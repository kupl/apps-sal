N, C = list(map(int, input().split()))

tv = [[0]*C for _ in range(100000)]
for _ in range(N):
    s, t, c = list(map(int, input().split()))
    for i in range(s-1, t): tv[i][c-1] = 1
    
print((max([sum(tv[i]) for i in range(100000)])))

