N, K = map(int, input().split())
dic = {}
dic['s'], dic['p'], dic['r'] = map(int, input().split())
T = input()
score = [0] * N
for i in range(N):
    if i >= K and T[i] == T[i - K] and score[i - K] > 0:
        continue
    score[i] = dic[T[i]]
print(sum(score))
