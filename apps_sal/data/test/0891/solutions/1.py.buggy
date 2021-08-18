import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
S = input().strip()

ANS = ["?"] * n

for i in range(n - 1):
    if S[i] == "B":
        if S[i - 1] == "B" or S[i + 1] == "B":
            ANS[i] = "B"

    else:
        if S[i - 1] == "W" or S[i + 1] == "W":
            ANS[i] = "W"

if S[n - 1] == "B":
    if S[n - 2] == "B" or S[0] == "B":
        ANS[n - 1] = "B"

else:
    if S[n - 2] == "W" or S[0] == "W":
        ANS[n - 1] = "W"


COMP = []

count = 1
now = ANS[0]

for i in range(1, n):
    if ANS[i] == ANS[i - 1]:
        count += 1
    else:
        COMP.append([now, count])
        count = 1
        now = ANS[i]

COMP.append([now, count])
hosei = 0

if len(COMP) == 1:
    if COMP[0][0] != "?":
        print(S)
    else:
        if k % 2 == 0:
            print(S)
        else:
            ANS = []
            for s in S:
                if s == "B":
                    ANS.append("W")
                else:
                    ANS.append("B")
            print("".join(ANS))
    return

if COMP[0][0] == "?" and COMP[-1][0] == "?":
    hosei = COMP[-1][1]
    COMP.pop()
    COMP[0][1] += hosei

ANS2 = []

LEN = len(COMP)
if COMP[0][0] != "?":
    COMP.append(COMP[0])

for i in range(LEN):
    if COMP[i][0] != "?":
        ANS2.append(COMP[i])
    else:
        x = COMP[i][1]

        if x <= k * 2:
            if COMP[i - 1][0] == COMP[i + 1][0]:
                ANS2.append([COMP[i - 1][0], x])

            else:
                ANS2.append([COMP[i - 1][0], x // 2])
                ANS2.append([COMP[i + 1][0], x // 2])

        else:
            ANS2.append([COMP[i - 1][0], k])
            ANS2.append(["?", x - 2 * k])
            ANS2.append([COMP[i + 1][0], k])

# print(ANS2)

GOAL = []
for x, y in ANS2:
    if x != "?":
        GOAL += [x] * y
    else:
        if GOAL != []:
            if GOAL[-1] == "B":
                t = 0
            else:
                t = 1
        else:
            if ANS2[-1][0] == "B":
                t = 0
            else:
                t = 1

        for j in range(y):
            if j % 2 == 0:
                if t == 0:
                    GOAL.append("W")
                else:
                    GOAL.append("B")
            else:
                if t == 0:
                    GOAL.append("B")
                else:
                    GOAL.append("W")

GOAL = GOAL[hosei:] + GOAL[:hosei]

print("".join(GOAL))
