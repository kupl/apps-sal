import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
bc = [list(map(int, input().split())) for _ in range(m)]
bc.sort(key = lambda x: x[1], reverse = True)

for i in range(m):
    if a[0] >= bc[i][1]:
        break
    else:
        cnt = 0
        while cnt < bc[i][0]:
            heapq.heapreplace(a, bc[i][1])
            cnt += 1

print(sum(a))
