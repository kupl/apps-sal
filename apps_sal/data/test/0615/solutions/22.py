N = int(input())

A = [0] * N
S = 0
for i, a in enumerate(input().split()):
    S += int(a)
    A[i] = S

answer = S

B = 0
D = 0

for C in range(1, N - 2):
    D = max(D, C + 1)
    SB = A[B]
    SC = A[C] - A[B]
    SD = A[D] - A[C]
    SE = S - A[D]
    left_score = abs(SB - SC)
    while True:
        B_ = B + 1
        SB_ = A[B_]
        SC_ = A[C] - SB_
        x = abs(SB_ - SC_)
        if left_score > x:
            B, SB, SC, left_score = B_, SB_, SC_, x
            continue
        break

    right_score = abs(SE - SD)
    while True:
        D_ = D + 1
        SD_ = A[D_] - A[C]
        SE_ = S - A[D_]
        x = abs(SD_ - SE_)
        if right_score > x:
            D, SD, SE, right_score = D_, SD_, SE_, x
            continue
        break

    score = max(SB, SC, SD, SE) - min(SB, SC, SD, SE)
    answer = min(score, answer)
print(answer)
