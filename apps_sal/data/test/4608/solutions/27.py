N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input()) - 1  # 配列に対応
index = 0
trials = -1
for i in range(N):
    index = A[index]
    if index == 1:
        trials = i + 1
        break
print(trials)
