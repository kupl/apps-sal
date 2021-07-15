n, k, m = list(map(int, input().split()))
scores = list(map(int,input().split()))

N_score = m * n - sum(scores)

if N_score < 0:
    print((0))
elif k < N_score:
    print((-1))
else:
    print(N_score)

