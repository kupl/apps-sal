import sys


def 解():
    iN = int(input())
    aP = [[int(_) for _ in sLine.rstrip("\n").split()] for sLine in sys.stdin.readlines()]

    i最遠 = max([abs(iX) + abs(iY) for iX, iY in aP])

    iMod = sum(aP[0]) % 2
    for i in range(1, iN):
        if sum(aP[i]) % 2 != iMod:
            print("-1")
            return
    a腕 = [1]
    if iMod == 0:
        a腕 = [1, 1]
    for i in range(32):
        a腕.append(a腕[-1] * 2)
        if i最遠 // 2 < a腕[-1]:
            break
    a腕.reverse()
    iLen腕 = len(a腕)
    print(iLen腕)
    print((" ".join([str(_) for _ in a腕])))
    aRet = []
    for aE in aP:
        aCommand = []
        iX = aE[0]
        iY = aE[1]
        for i in range(iLen腕):
            if abs(iX) > abs(iY):
                if iX < 0:
                    iX += a腕[i]
                    aCommand.append("L")
                else:
                    iX -= a腕[i]
                    aCommand.append("R")
            else:
                if iY < 0:
                    iY += a腕[i]
                    aCommand.append("D")
                else:
                    iY -= a腕[i]
                    aCommand.append("U")
        aRet.append("".join(aCommand))
    sys.stdout.write("\n".join(aRet) + "\n")


def __starting_point():
    解()


__starting_point()
