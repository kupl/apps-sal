import math

N,D = list(map(int, input().split()))

X = [[0] * D  for i in range(N)]

for i in range(N):
    X[i] = list(map(int, input().split()))

count = 0
for i in range(N):
    ran = list(range(i+1,N))
    for j in ran:
        dis = 0
        for d in range(D):
            dis += (X[i][d] - X[j][d]) *  (X[i][d] - X[j][d])
        
        dis = math.sqrt(dis)
        if dis.is_integer() == True:
            count += 1

print(count)

