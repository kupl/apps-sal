from operator import itemgetter
N = int(input())
red = [list(map(int, input().split())) for i in range(N)]
red.sort()
blue = [list(map(int, input().split())) for i in range(N)]
blue.sort()
ans = 0
for i in range(N):
    x, y = blue[i]
    l = []
    for j in range(N):
        try:
            if x > red[j][0] and y > red[j][1]:
                l.append(red[j])
        except IndexError:
            break
    try:
        l.sort(key=itemgetter(1), reverse=True)
        red.remove(l[0])
    except IndexError:
        pass
print(N - len(red))
