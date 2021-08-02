n, m, k = list(map(int, input().split()))
discard = list(map(int, input().split()))
startK = (int(discard[0] / k) + (discard[0] % k != 0)) * k
step = 0
id = 0
while True:
    #print("startK", startK)
    disnum = 0
    while (id < m and startK >= discard[id]):
        disnum += 1
        #print(discard[id], end = ' ')
        id += 1
    startK += disnum

    if disnum == 0:
        if id == m: break;
        startK += int((discard[id] - startK) / k + ((discard[id] - startK) % k != 0)) * k
    else:
        step += 1
        # print()
print(step)
