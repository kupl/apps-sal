import sys
input = sys.stdin.readline

n, z = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()


def match(cut):
    i = 0
    j = cut

    ANS = 0

    for i in range(cut):
        while j < n and X[j] - X[i] < z:
            j += 1
        if j == n:
            break
        else:
            ANS += 1
            j += 1
            # print(i,j)

    return ANS


MIN = 1
MAX = n - 1

while MAX - MIN > 1:
    MID0 = (MIN + MAX) // 2 - 1
    MID1 = (MIN + MAX) // 2

    ANS2 = match(MID0)
    ANS3 = match(MID1)

    if ANS2 == ANS3:
        print(ANS2)
        return

    if ANS2 > ANS3:
        MAX = MID0
    else:
        MIN = MID1

print(max(match(MIN), match(MAX)))
