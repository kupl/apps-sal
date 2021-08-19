#! /usr/bin/python
# kmwho
# Codeforces 401 D2

def main():
    n = int(input())
    sher = [int(c) for c in input().strip()]
    mori = [int(c) for c in input().strip()]
    counts = [0] * 10
    countm = [0] * 10

    for dm in mori:
        countm[dm] += 1

    # Defence
    countdef = 0
    for ds in sher:
        defended = False
        for dm in range(ds, 10):
            if countm[dm] > 0:
                countm[dm] -= 1
                defended = True
                break
        if not defended:
            countdef += 1
            for dm in range(n):
                if countm[dm] > 0:
                    countm[dm] -= 1
                    break

    print(countdef)

    # Offence
    countdm = [0] * 10
    for dm in mori:
        countm[dm] += 1

    countoff = 0
    for ds in sher:
        attacked = False
        for dm in range(ds + 1, 10):
            if countm[dm] > 0:
                countm[dm] -= 1
                attacked = True
                countoff += 1
                break
        if not attacked:
            for dm in range(n):
                if countm[dm] > 0:
                    countm[dm] -= 1
                    break

    print(countoff)


main()
