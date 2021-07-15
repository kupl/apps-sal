n, t = list(map(int,input().split()))
bo = [[0.0]*(n+1) for i in range(n+1)]
while t > 0:
    bo[0][0] += 1
    for i in range(n):
        for j in range(0,i+1):
            if bo[i][j] > 1.0:
                temp = (bo[i][j] - 1)/ 2
                bo[i][j] = 1.0
                bo[i+1][j] += temp
                bo[i+1][j+1] += temp
    t -= 1

num = 0
for i in range(n):
    for j in range(0,i+1):
        if bo[i][j] >= 1.0:
            num += 1
print(num)

