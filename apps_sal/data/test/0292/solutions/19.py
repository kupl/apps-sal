import sys


def main():
    rdl = list(map(int, input().split()))
    obx(rdl[0], rdl[1], 0, 1)


def obx(lvl, ind, kl, current):
    if lvl == 0:
        print(int(kl))
        return
    all = 0
    for i in range(lvl + 1):
        all += 2**i
    all -= 1

    if ind > (2**(lvl)) / 2:
        if current == 1:
            kl += all / 2 + 1
        else:
            kl += 1
            current *= -1
        obx(lvl - 1, ind - (2**lvl) / 2, kl, current)
    else:
        if current == -1:
            kl += all / 2 + 1
        else:
            kl += 1
            current *= -1
        obx(lvl - 1, ind, kl, current)


main()
