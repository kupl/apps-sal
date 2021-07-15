n, t = map(int, input().split())

t = min(2000, t)
L = [ [0.0]*n for i in range(n) ]
for _ in range(t) :
    L[0][0] += 1.0
    for i in range(n-1) :
        for j in range(i+1) :
            if L[i][j] > 1.0 :
                x = (L[i][j] - 1.0) / 2
                L[i+1][j] += x
                L[i+1][j+1] += x
                L[i][j] = 1.0

ans = 0
for i in range(n) :
    for j in range(i+1) :
        if L[i][j] > 0.9999999999 :
            ans += 1

print(ans)
