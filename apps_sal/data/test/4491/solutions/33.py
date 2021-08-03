

N = int(input())

upper = list(map(int, input().split()))
down = list(map(int, input().split()))

scores = []
for i in range(N):
    score = 0
    flag = 0
    for j in range(N):
        if i == j and flag == 0:
            score += upper[j]
            score += down[j]
            flag = 1
        elif flag == 0:
            score += upper[j]
        elif flag == 1:
            score += down[j]
    scores.append(score)

print(max(scores))
