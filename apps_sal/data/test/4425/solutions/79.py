import math
N, M = map(int, input().split())

if M == 1:
    print(1)
    return


prob = 0
for i in range(1, N + 1):
    if i >= M:
        prob += 1 / N
    else:
        prob += ((1 / N) * 1 / 2**math.ceil(math.log(M / i, 2)))

print(prob)
