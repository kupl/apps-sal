import math
X, N = map(int, input().split())
P = list(map(int, input().split()))
ans_1 = X
ans_2 = X
while True:
    if ans_1 not in P:
        print(ans_1)
        return
    ans_1 -= 1

    if ans_2 not in P:
        print(ans_2)
        return
    ans_2 += 1
