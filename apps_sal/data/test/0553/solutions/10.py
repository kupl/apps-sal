# import time
# start = time.time()
n = int(input())
codes = [input() for i in range(n)]
mindist = 6
for i in range(n-1):
    for j in range(i+1, n):
        d = sum([x!=y for x,y in zip(codes[i], codes[j])])
        # for k in range(6):
            # d += codes[i][k] != codes[j][k]
        if mindist > d:
            mindist = d
if (n == 1):
    print(6)
else:
    print(max(0, (mindist-1)//2))
# print(time.time()-start)
# print(mindist)

