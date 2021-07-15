n,m = list(map(int,input().split()))
h = list(map(int,input().split()))
ab = [list(map(int,input().split())) for _ in range(m)]

place = [True]*n

for i in range(m):
    a,b = ab[i][0],ab[i][1]
    if h[a-1] < h[b-1]:
        place[a-1] = False
    elif h[a-1] == h[b-1]:
        place[a-1] = False
        place[b-1] = False
    else:
        place[b-1] = False

print((place.count(True)))

