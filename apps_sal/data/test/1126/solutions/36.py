S = input().split()

N, X, M = [int(s) for s in S]

init = X
count = 0
box = [0] * (M + 2)

for i in range(M):
    box[i] = X
    X = (X ** 2) % M

T = len(set(box))

for t in range(T):
    if box[t] == box[T]:
        break


print(sum(box[:t]) + ((N - t) // (T - t)) * sum(box[t:T]) + sum(box[t:t + (N - t) % (T - t)]))
