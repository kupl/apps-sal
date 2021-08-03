n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]

ren = []

for i in range(m):
    if ab[i][0] == 1:
        ren.append(ab[i][1])
    elif ab[i][1] == n:
        ren.append(ab[i][0])

cnt = len(ren)

if len(set(ren)) == cnt:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
