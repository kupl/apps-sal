import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    S = input().strip()
    ANSP = []
    f = 0
    l = len(S) - 1
    while f < l and S[f] == S[l]:
        ANSP.append(S[f])
        f += 1
        l -= 1
    if f == l or f == l + 1:
        print(S)
        continue
    S2 = S[f:l + 1]
    SS2 = []
    for s in S2:
        SS2.append(s)
        SS2.append('$')
    SS2.pop()
    LEN = len(SS2)
    i = 0
    j = 0
    R = [0] * LEN
    while i < LEN:
        while i - j >= 0 and i + j < LEN and (SS2[i - j] == SS2[i + j]):
            j += 1
        R[i] = j
        k = 1
        while i - k >= 0 and i + k < LEN and (k + R[i - k] < j):
            R[i + k] = R[i - k]
            k += 1
        i += k
        j -= k
    MAX = 0
    for i in range(LEN):
        if i - R[i] + 1 == 0 or i + R[i] == LEN:
            if MAX < R[i]:
                MAX = R[i]
                MAXind = i
    S3 = SS2[MAXind - MAX + 1:MAXind + MAX]
    SS3 = []
    for s in S3:
        if s != '$':
            SS3.append(s)
    sys.stdout.write(''.join(ANSP) + ''.join(SS3) + ''.join(ANSP[::-1]) + '\n')
