N = int(input())
A = list(map(ord, list(input())))
S = [0] * 150
for i in range(N):
    S[A[i]] += 1
Pokemon = len(S) - S.count(0)
L = 0
R = N
while(R - L > 1):
    M = (R + L) // 2
    l = 0
    r = 0
    S = [0] * 150
    count = 0
    is_ok = False
    while r < l + M:
        if S[A[r]] == 0:
            count += 1
        S[A[r]] += 1
        r += 1
    if count == Pokemon:
        is_ok = True
    while r < N and not is_ok:
        if S[A[l]] == 1:
            count -= 1
        S[A[l]] -= 1
        if S[A[r]] == 0:
            count += 1
        S[A[r]] += 1
        l += 1
        r += 1
        if count == Pokemon:
            is_ok = True
    if is_ok:
        R = M
    else:
        L = M
print(R)
