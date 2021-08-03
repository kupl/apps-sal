from heapq import heappush, heappop

N, K = [int(s) for s in input().split()]
songs = []
beauties = set()
for _ in range(N):
    t, b = [int(s) for s in input().split()]
    beauties.add(b)
    songs.append((t, b))
songs = sorted(songs, key=lambda x: x[1], reverse=True)
max_pleasure = 0
total_length = 0
max_lengths = []
for i in range(K):
    total_length += songs[i][0]
    heappush(max_lengths, songs[i][0])
    max_pleasure = max(max_pleasure, total_length * songs[i][1])
for i in range(K, N):
    if max_lengths[0] < songs[i][0]:
        min_length = heappop(max_lengths)
        heappush(max_lengths, songs[i][0])
        total_length = total_length - min_length + songs[i][0]
        max_pleasure = max(max_pleasure, total_length * songs[i][1])
print(max_pleasure)
