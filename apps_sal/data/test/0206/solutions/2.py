from collections import deque


def gcd(a, b):
    b = abs(b)
    while b != 0:
        r = a % b
        a, b = b, r
    return a


M, A, B = list(map(int, input().split()))
X = [1] + [0] * (10**6)
Y = [0]
s = 1
t = 1
g = gcd(A, B)
for N in range(1, M + 1):
    if N >= A + B + g and (M - N + 1) % g == 0:
        ss = Y[N - 1] - Y[N - g - 1]
        dd = (Y[N - 1] - Y[N - 2]) - (Y[N - g - 1] - Y[N - g - 2])
        t += ss * (M - N + 1) // g + dd * g * ((M - N + 1) // g) * ((M - N + 1) // g + 1) // 2
        break
    elif N >= A and X[N - A]:
        que = deque([N])
        X[N] = 1
        s += 1
        while len(que):
            i = deque.pop(que)
            if i >= B and X[i - B] == 0:
                deque.append(que, i - B)
                X[i - B] = 1
                s += 1
            if i + A < N and X[i + A] == 0:
                deque.append(que, i + A)
                X[i + A] = 1
                s += 1
    t += s
    Y.append(t)
print(t)
