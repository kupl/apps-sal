n = int(input())
csf = [list(map(int, input().split())) for _ in range(n - 1)]
for i in range(n):
    time = 0
    while True:
        if i == n - 1:
            print(time)
            break
        if time < csf[i][1]:
            time = csf[i][1] + csf[i][0]
        elif time % csf[i][2] == 0:
            time += csf[i][0]
        else:
            time += csf[i][0] + csf[i][2] - time % csf[i][2]
        i += 1
