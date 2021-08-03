N = int(input())
if N == 0:
    print(0)
    return
if N > 0:
    S = bin(N)[2:]
    S = list(S[::-1])
    S = list(map(int, S))
    S += [0] * 1000
    i = 0
    while True:
        S[i + 1] += S[i] // 2
        S[i] = S[i] % 2
        if i % 2 == 1:
            S[i + 1] = S[i + 1] + S[i]
        i += 1
        if i == len(S) - 1:
            break
    S = list(map(str, S))
    S = list(reversed(S))
    S = "".join(S)
    print(int(S))
else:
    N = abs(N)
    S = bin(N)[2:]
    S = list(S[::-1])
    S = list(map(int, S))
    S += [0] * 1000
    i = 0
    while True:
        S[i + 1] += S[i] // 2
        S[i] = S[i] % 2
        if i % 2 == 0:
            S[i + 1] = S[i + 1] + S[i]
        i += 1
        if i == len(S) - 1:
            break
    S = list(map(str, S))
    S = list(reversed(S))
    S = "".join(S)
    print(int(S))
