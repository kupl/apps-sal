(n, m) = list(map(int, input().split()))
song_end = [None] * n
for i in range(n):
    (c, t) = list(map(int, input().split()))
    song_end[i] = (song_end[i - 1] if i > 0 else 0) + c * t
moments = list(map(int, input().split()))
curr_song = 0
res = []
for mom in moments:
    while mom > song_end[curr_song]:
        curr_song += 1
    res.append(str(curr_song + 1))
print('\n'.join(res))
