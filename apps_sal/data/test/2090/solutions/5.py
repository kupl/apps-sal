import heapq

n, k = map(int, input().split())

songs = [(0, 0) for i in range(n)]

for i in range(n):
    songs[i] = tuple(map(int, input().split()))

songs.sort(key=lambda x: x[1], reverse=True)

heap = []
max_ = 0
length = 0
for i in range(n):
    if i >= k:
        l = heapq.heappushpop(heap, songs[i][0])
        length = length - l + songs[i][0]
    else:
        length += songs[i][0]
        heapq.heappush(heap, songs[i][0])
    max_ = max(max_, length * songs[i][1])

print(max_)
