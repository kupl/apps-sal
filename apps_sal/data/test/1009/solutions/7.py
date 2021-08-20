import math
(n, k) = map(int, input().split())
data = list(map(int, input().split()))
colvo_1_cor = k * 2 - n
colvo_2_cor = k - colvo_1_cor
answer = []
if colvo_1_cor > n:
    colvo_1_cor = n
for i in range(colvo_1_cor):
    answer.append(data[-1])
    data.pop()
if len(data) > 0:
    index1 = 0
    index2 = len(data) - 1
    while index1 != len(data) // 2 + 1:
        answer.append(data[index1] + data[index2])
        index1 += 1
        index2 -= 1
print(max(answer))
