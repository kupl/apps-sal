totIts = int(input())
colCts = list(map(int, input().split()))

for i in range(totIts):
    currColCt = colCts[i]
    for j in [1, 2, 4, 3]:
        c = j
        if c != 4:
            print(c, end=" ")
            for k in range(0, currColCt - 1):
                print(c + 3 * (2**k), end=" ")
                c = c + 3 * (2**k)
        else:
            print(c, end=" ")
            for k in range(0, currColCt - 1):
                print(c + 6 * (2**k), end=" ")
                c = c + 6 * (2**k)
        print("")
