S = input()
T = input()
(N, M) = (len(S), len(T))


def calc(s, t):
    X = [0] * len(s)
    j = 0
    for i in range(len(s)):
        if j >= len(t):
            X[i] = j
        elif s[i] == t[j]:
            X[i] = j + 1
            j += 1
        else:
            X[i] = X[i - 1]
    return [0] + X


(A, B) = (calc(S, T), calc(S[::-1], T[::-1])[::-1])
(l, r) = (0, N)
while r - l > 1:
    m = (l + r) // 2
    C = [A[i] + B[i + m] for i in range(N - m + 1)]
    if max(C) >= M:
        l = m
    else:
        r = m
print(l)
