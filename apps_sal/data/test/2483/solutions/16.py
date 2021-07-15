n,c = list(map(int,input().split()))

t = [[0 for i in range(100001)] for j in range(c)]

for i in range(n):
    si,ti,ci = list(map(int,input().split()))
    for j in range(si,ti+1):
        t[ci-1][j] = 1
print((max(sum(t[j][i] for j in range(c)) for i in range(100001))))

