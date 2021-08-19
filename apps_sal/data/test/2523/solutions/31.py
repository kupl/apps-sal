S = [0] + list(map(int, list(input())))
N = len(S) - 1


def change(s, c):
    if c == 0:
        return s
    else:
        return 1 - s


def check(k):
    count = [0] * (N + 1)
    T = S.copy()
    for i in range(1, N + 1):
        c = count[i - 1]
        s = change(S[i], c)
        if i < N - k + 2:
            T[i] = 0
            if s == 1:
                count[i] = (c + 1) % 2
            else:
                count[i] = c
        else:
            T[i] = s
            count[i] = c
    n = 0
    for t in T[1:]:
        if t == 1:
            break
        n += 1
    return n >= k


left = 1
right = N
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
if right == N and check(N):
    print(N)
else:
    print(left)
