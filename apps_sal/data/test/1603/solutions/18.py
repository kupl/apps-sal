import sys
# Never really use this value
numberOfStones = int(sys.stdin.readline())
# Stones in given order
stonelistV = (list(map(int, sys.stdin.readline().split())))
# stones in ascending order
stonelistU = sorted(stonelistV)
# print(stonelistU)
# Hold the computed sums
du = [0] * 1
dv = [0] * 1
# Compute the sums
for stone in stonelistV:
    dv.append(dv[-1] + stone)
for stone in stonelistU:
    du.append(du[-1] + stone)

numberOfQuestions = int(sys.stdin.readline())
for q in range(numberOfQuestions):
    questions = list(map(int, sys.stdin.readline().split()))
    if questions[0] == 1:
        answer = dv[questions[2]] - dv[questions[1] - 1]
    if questions[0] == 2:
        answer = du[questions[2]] - du[questions[1] - 1]
    print(answer)
