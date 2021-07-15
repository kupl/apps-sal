
tt = int(input())

for loop in range(tt):

    n,k = list(map(int,input().split()))

    lis = [ [0] * n for i in range(n) ]

    ns = 0
    for si in range(n):

        if ns == k:
            break

        for i in range(n):

            lis[(si+i)%n][i] = 1
            ns += 1

            if ns == k:
                break
        else:
            continue
        break

    R = []
    for i in range(n):
        now = 0
        for j in range(n):
            now += lis[i][j]
        R.append(now)

    C = []
    for i in range(n):
        now = 0
        for j in range(n):
            now += lis[j][i]
        C.append(now)

    print((max(R)-min(R))**2 + (max(C)-min(C))**2)
    for i in lis:
        print("".join(map(str,i)))

