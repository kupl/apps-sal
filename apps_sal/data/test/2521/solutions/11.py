import heapq
n = int(input())
a = list(map(int, input().split()))
pres = a[:n]
heapq.heapify(pres)
apresum = [0] * (n + 1)
aps = sum(pres)
apresum[0] = aps
posts = list([-1 * x for x in a[::-1][:n]])
heapq.heapify(posts)
apossum = [0] * (n + 1)
aqs = sum(posts)
apossum[0] = aqs
for i in range(1, n + 1):
    tempprea = a[n + i - 1]
    tempposta = -1 * a[2 * n - i]
    heapq.heappush(pres, tempprea)
    tempprepop = heapq.heappop(pres)
    aps += tempprea - tempprepop
    apresum[i] = aps
    heapq.heappush(posts, tempposta)
    temppostpop = heapq.heappop(posts)
    aqs += tempposta - temppostpop
    apossum[i] = aqs
print((max([x + y for x, y in zip(apresum, apossum[::-1])])))
