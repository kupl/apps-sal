n = int(input())
ai = list(map(int,input().split()))
photos = [[0]*1000000 for i in range(2)]
for i in range(n):
    photos[0][ai[i]-1] += 1
    photos[1][ai[i]-1] = i
max_likes = max(photos[0])
min_ind = 1000000
ans = 0
for i in range(1000000):
    if photos[0][i] != 0 and max_likes == photos[0][i]:
        if min_ind > photos[1][i]:
            min_ind = photos[1][i]
            ans = i+1
print(ans)

