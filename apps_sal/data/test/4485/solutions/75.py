n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]

ren = []

for i in range(m):
    if ab[i][0] == 1:
        ren.append(ab[i][1])
    elif ab[i][1] == n:
        ren.append(ab[i][0])

ren.sort()
if ren[0] == 1 and ren[-1] == n:
    print("POSSIBLE")
else:
    for i in range(len(ren) - 1):
        if ren[i] == ren[i + 1]:
            print("POSSIBLE")
            break
    else:
        print("IMPOSSIBLE")
