K = int(input())


def NS(N):
    NS = 0
    while N > 0:
        NS += N % 10
        N //= 10
    return NS


(answer, diff) = (0, 1)
for i in range(K):
    answer += diff
    print(answer)
    if diff < (answer + diff) / NS(answer + diff):
        diff *= 10
