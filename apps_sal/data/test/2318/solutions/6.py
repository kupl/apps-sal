import sys
input = iter(sys.stdin.read().splitlines()).__next__

n = int(input())


def prep(s):
    S = []
    lc = None
    count = 0
    for c in s:
        if c != lc and count:
            S.append((lc, count))
            count = 0
        count += 1
        lc = c
    if count:
        S.append((lc, count))
    return S


for _ in range(n):
    t = input()
    s = input()

    T = prep(t)
    S = prep(s)
    if len(T) == len(S):
        for i in range(len(T)):
            if T[i][0] != S[i][0] or T[i][1] > S[i][1]:
                break
        else:
            print('YES')
            continue
        print('NO')
    else:
        print('NO')
