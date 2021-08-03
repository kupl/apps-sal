N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = []
for a, b in zip(A, A[1:]):
    X.append(a ^ b)
X.append(A[-1] ^ A[0])

Y = []
for a, b in zip(B, B[1:]):
    Y.append(a ^ b)
Y.append(B[-1] ^ B[0])


def z_algorithm(s):
    N = len(s)
    ret = [0] * N
    ret[0] = N
    i, j = 1, 0
    while i < N:
        while i + j < N and s[j] == s[i + j]:
            j += 1
        ret[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < N and k + ret[k] < j:
            ret[i + k] = ret[k]
            k += 1
        i += k
        j -= k
    return ret


za = z_algorithm(X + [-1] + Y + Y)
for i in range(N):
    if za[-N - i] == N:
        print(i, A[i] ^ B[0])
