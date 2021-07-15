N, D = map(int, input().split())

X = [input().split() for i in range(N)]

count = 0
d_2 = 0
d = 0

for i in range(1, N):
    for j in range(0, i):
        d_2 = 0
        d = 0
        for k in range(D):
            d_2 += (float(X[i][k]) - float(X[j][k]))**2
        d = d_2**(1/2)
        if d.is_integer() == True:
            count += 1

print("{}".format(count))
