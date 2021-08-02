def givelen(_______):
    tot = 0
    while _______:
        _______ //= 10
        tot += 1
    return tot


for _ in range(int(input())):
    end = int(input())
    l = []
    secon = sec = ans = currlen = last = 0

    while end > 0:
        last += 1
        l.append(last)
        currlen += givelen(last)
        secon = end
        end -= currlen

    for i in range(len(l)):
        sec = secon
        secon -= givelen(l[i])
        if secon <= 0:
            ans = str(l[i])[sec - 1]
            break
    print(ans)
