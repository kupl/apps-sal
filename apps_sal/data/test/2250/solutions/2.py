import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    X = []
    prev = S[0]
    c = 0
    for i, s in enumerate(S):
        if s == prev:
            c += 1
        else:
            X.append(c)
            prev = s
            c = 1
    if not X:
        X.append(N + 2)
    elif prev == S[0]:
        X[0] += c
    else:
        X.append(c)
    print(sum([x // 3 for x in X]))
