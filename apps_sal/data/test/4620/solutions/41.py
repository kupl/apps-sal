N = int(input())
l = []
for i in range(N - 1):
    c, s, f = map(int, input().split())
    l.append([c, s, f])

for i in range(N - 1):
    time = l[i][1] + l[i][0]
    for j in range(i + 1, N - 1):
        if time - l[j][1] >= 0:
            wait = time % l[j][2]
            if wait == 0:
                time += l[j][0]
            else:
                time += l[j][2] - wait + l[j][0]
        else:
            time = l[j][1] + l[j][0]
    print(time)
print(0)
