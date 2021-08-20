from collections import defaultdict
X = list(map(int, input().split()))
Answers = []
for i in range(X[0]):
    Answers.append(input())
points = list(map(int, input().split()))
Sum = 0
for i in range(X[1]):
    Temp = defaultdict(int)
    for j in range(X[0]):
        Temp[Answers[j][i]] += 1
    Sum += points[i] * max(Temp.values())
print(Sum)
