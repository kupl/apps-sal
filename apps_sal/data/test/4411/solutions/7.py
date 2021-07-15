import heapq
n, k = list(map(int, input().split()))
length = 2 * (10 ** 5)
llist = [[] for x in range(length + 1)]
rlist = [[] for x in range(length + 1)]
flag = [0] * (length + 1)
for i in range(n):
    l, r = list(map(int, input().split()))
    llist[l].append([i + 1, r])
    rlist[r].append([i + 1, l])
heap = []
ans = []
now = 0
for i in range(length):
    i += 1
    for j in llist[i]:
        now += 1
        currents = j[0]
        r = j[1]
        flag[currents] = 1
        heapq.heappush(heap, [-1 * r, currents])
    for j in rlist[i - 1]:
        currents = j[0]
        if flag[currents] == 1:
            now -= 1
            flag[currents] = 0
    while now > k:
        removing = heapq.heappop(heap)
        currents = removing[1]
        if flag[currents] == 1:
            ans.append(currents)
            now -= 1
            flag[currents] = 0
print(len(ans))
print(" ".join(map(str, ans)))

