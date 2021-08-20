import math
NN = int(input())
AI = list(map(int, input().split()))
(XX, FF) = list(map(int, input().split()))
length = len(AI)
extra = 0
for xx in AI:
    if xx > XX:
        extra += math.ceil((xx - XX) / (XX + FF))
print(extra * FF)
