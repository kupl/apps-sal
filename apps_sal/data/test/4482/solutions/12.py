N = int(input())
List = list(map(int, input().split()))
sumS = 0
for i in range(N):
    sumS += List[i]
trial = sumS // N
mid = 0
res = 10000000
for i in range(N):
    trial += i
    mid = 0
    for j in range(N):
        mid += (trial - List[j]) ** 2
    res = min(res, mid)
print(res)
