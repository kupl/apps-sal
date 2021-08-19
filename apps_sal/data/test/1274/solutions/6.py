import heapq

N, M = list(map(int, input().split()))


rinsetuList = [[] for _ in range(100001)]

for _ in range(N):
    A, B = list(map(int, input().split()))
    rinsetuList[A].append(B)

# print(rinsetuList[:M+1])

work_list = []
hpq = heapq.heapify(work_list)

ans = 0
for rinsetu in rinsetuList[:M + 1]:
    for money in rinsetu:
        heapq.heappush(work_list, money * (-1))
    if(len(work_list) != 0):
        ans += heapq.heappop(work_list) * (-1)

#    print(ans)
#    print(work_list)

print(ans)
