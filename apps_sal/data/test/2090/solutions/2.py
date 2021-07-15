import heapq
n, k = list(map(int, input().split()))
music = []
for i in range(n):
    length, beauty = list(map(int, input().split()))
    music.append((beauty, length))
music.sort(reverse=True)
s = []
ma = 0
sumlength = 0
# print(music)
for i in range(n):
    if len(s) == k:
        t = heapq.heappushpop(s, music[i][1])
    else:
        heapq.heappush(s, music[i][1])
        t = 0
    sumlength += music[i][1] - t
    # print(sumlength)
    ma = max(sumlength * music[i][0], ma)
print(ma)

