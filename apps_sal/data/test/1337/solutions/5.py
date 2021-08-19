from sys import stdin, stdout
n = int(stdin.readline())
d = {}
languages = list(map(int, stdin.readline().split()))
for l in languages:
    if l not in d:
        d[l] = 1
    else:
        d[l] += 1
m = int(stdin.readline())
movies = []
voice = list(map(int, stdin.readline().split()))
for i in range(m):
    if voice[i] in d:
        movies.append([d[voice[i]], 0, i])
    else:
        movies.append([0, 0, i])
subtitles = list(map(int, stdin.readline().split()))
for i in range(m):
    if subtitles[i] in d:
        movies[i][1] = d[subtitles[i]]
stdout.write(str(sorted(movies)[-1][-1] + 1))
