# 26
H = int(input())


def getAns(x):
    if x <= 1: return 1
    return 2 * getAns(x // 2) + 1


ans = getAns(H)

print(ans)
