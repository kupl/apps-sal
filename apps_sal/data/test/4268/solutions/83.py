import math

N,D = list(map(int,input().split()))

ary = []
for _ in range(N):
    ary.append(list(map(int,input().split())))

counter = 0
ary_len = len(ary)
for i in range(ary_len - 1):
    for j in range(i+1,ary_len):
        tmp = 0
        for k in range(D):
            tmp += pow(abs(ary[i][k]-ary[j][k]),2)
        if math.sqrt(tmp) % 1 == 0:
            counter += 1
print(counter)

