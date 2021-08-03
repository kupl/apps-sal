n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

ANS = 0
for i in range(k):
    ex = 0
    so = 0
    for l in range(n):
        if l % k == i:
            continue
        if A[l] == 1:
            ex += 1
        else:
            so += 1

    if ANS < abs(ex - so):
        ANS = abs(ex - so)

print(ANS)
