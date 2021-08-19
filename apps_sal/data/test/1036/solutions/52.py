import sys
sys.setrecursionlimit(10 ** 6)
(N, K) = list(map(int, input().split()))
S = input()
S = S + S


def judge(a, b):
    if a == b:
        return a
    elif a == 'R':
        if b == 'S':
            return a
        else:
            return b
    elif a == 'P':
        if b == 'R':
            return a
        else:
            return b
    elif a == 'S':
        if b == 'R':
            return b
        else:
            return a


for k in range(K):
    N = len(S)
    T = ''
    for i in range(0, N, 2):
        T += judge(S[i], S[i + 1])
    S = T + T
print(S[0])
