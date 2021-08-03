n, k = map(int, input().split())
coverd = 0
for i in range(0, n):
    start, end = map(int, input().split())
    coverd = coverd + (end - start + 1)

coverd = coverd % k
if (coverd != 0):
    coverd = k - coverd

print(coverd)
