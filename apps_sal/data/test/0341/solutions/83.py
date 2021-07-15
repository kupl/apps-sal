N, K = [int(_) for _ in input().split()]
R, S, P = [int(_) for _ in input().split()]
T = input()

s = {"r": P, "s": R, "p": S}

score = []
for i in range(N):
    if i < K:
        score.append(s[T[i]])
        continue
    if T[i] == T[i-K] and score[i-K] != 0:
        score.append(0)
    else:
        score.append(s[T[i]])

print((sum(score)))

