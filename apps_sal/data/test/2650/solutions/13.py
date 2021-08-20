import heapq
(n, q) = map(int, input().split())
belong = [-1 for i in range(n)]
rating = [0 for i in range(n)]
second = [[] for i in range(2 * 10 ** 5 + 5)]
for i in range(n):
    (a, b) = map(int, input().split())
    rating[i] = a
    belong[i] = b
    heapq.heappush(second[b], (-1 * a, i))
first = []
for i in range(2 * 10 ** 5 + 5):
    if second[i]:
        heapq.heappush(first, (-1 * second[i][0][0], second[i][0][1], i))
for i in range(q):
    (c, d) = map(int, input().split())
    before = belong[c - 1]
    belong[c - 1] = d
    heapq.heappush(second[d], (-1 * rating[c - 1], c - 1))
    if second[d][0][1] == c - 1:
        heapq.heappush(first, (rating[c - 1], c - 1, d))
    count = 0
    while second[before] and belong[second[before][0][1]] != before:
        heapq.heappop(second[before])
        count = 1
    if count and second[before]:
        heapq.heappush(first, (-1 * second[before][0][0], second[before][0][1], before))
    while not second[first[0][2]] or second[first[0][2]][0][1] != first[0][1]:
        heapq.heappop(first)
    print(first[0][0])
