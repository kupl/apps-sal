import sys


def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


(n, m) = [int(x) for x in sys.stdin.readline().strip().split(' ')]
songs = []
for i in range(n):
    cur = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    songs.append(cur)
queries = [int(x) for x in sys.stdin.readline().strip().split(' ')]
start_time = 0
intervals = []
cur_time = start_time
for i in range(0, len(songs)):
    song = songs[i]
    times = song[0]
    dur = song[1]
    new_time = cur_time + times * dur
    intervals.append(new_time)
    cur_time = new_time
queries = sorted(queries)
idx = 0
for q in queries:
    while q > intervals[idx]:
        idx += 1
    print(idx + 1)
