y = [int(x) for x in input().split(' ')]
n_m = []
for i in range(y[0]):
    p = [int(x) for x in input().split(' ')]
    n_m.append(p)
sum = 0
h = True
for i in range(y[0]-1, -1, -1):
    for j in range(y[1]-1, -1, -1):
        if n_m[i][j] == 0:
            if n_m[i+1][j] > n_m[i][j+1]:
                n_m[i][j] = n_m[i][j+1] - 1 
            else:
                n_m[i][j] = n_m[i+1][j] - 1 
        try:
            if j == 0:
                pass
            elif i == 0:
                pass
            elif n_m[i][j] <= n_m[i][j-1]:
                h = False
            elif n_m[i][j] <= n_m[i-1][j]:
                h = False
        except:
            pass
        if h == False:
            print(-1)
            return
        sum += n_m[i][j]
print(sum)

