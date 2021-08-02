
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

s = sum(A)


def solve():
    ans = 1
    idx = 1

    while idx * idx <= s:
        if s % idx == 0:
            if ok(s // idx):
                return s // idx
            if ok(idx):
                ans = idx
        idx += 1

    return ans


def ok(i):
    D = list([x for x in [a % i for a in A] if x != 0])
    D.sort()

    l = len(D)

    S = [0] * (l + 1)
    for j in range(l):
        S[j + 1] = S[j] + D[j]

    for j in range(l):
        if S[j] == i * (l - j) - (S[l] - S[j]) and S[j] <= K:
            return True

    return False


print((solve()))
