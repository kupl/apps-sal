(N, K, C) = list(map(int, input().split()))
S = input()
L = [0] * K
R = [0] * K
lpiv = 0
rpiv = N - 1
for i in range(K):
    while S[lpiv] == 'x':
        lpiv += 1
    while S[rpiv] == 'x':
        rpiv -= 1
    L[i] = lpiv
    R[i] = rpiv
    lpiv += C + 1
    rpiv -= C + 1
ans = 0
for i in range(K):
    if L[i] == R[K - i - 1]:
        print(L[i] + 1)
