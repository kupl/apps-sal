def solve(A, B, C, S):
    N = len(S)
    abc = [A, B, C]
    path = []
    for si in range(N - 1):
        (i, j) = S[si]
        if abc[i] == abc[j] == 0:
            print('No')
            return
        if abc[i] == 0:
            path.append('ABC'[i])
            abc[i] += 1
            abc[j] -= 1
            continue
        elif abc[j] == 0:
            path.append('ABC'[j])
            abc[j] += 1
            abc[i] -= 1
            continue
        (i2, j2) = S[si + 1]
        if not (abc[j] - 1 == 0 and abc[3 - i - j] == 0 and ({i2, j2} == {3 - i - j, j})):
            path.append('ABC'[i])
            abc[i] += 1
            abc[j] -= 1
            continue
        if not (abc[i] - 1 == 0 and abc[3 - i - j] == 0 and ({i2, j2} == {3 - i - j, i})):
            path.append('ABC'[j])
            abc[j] += 1
            abc[i] -= 1
            continue
        if abc[i] <= abc[j]:
            path.append('ABC'[i])
            abc[i] += 1
            abc[j] -= 1
        else:
            path.append('ABC'[j])
            abc[j] += 1
            abc[i] -= 1
    (i, j) = S[N - 1]
    if abc[i] == abc[j] == 0:
        print('No')
        return
    if abc[i] == 0:
        path.append('ABC'[i])
    else:
        path.append('ABC'[j])
    print('Yes')
    for c in path:
        print(c)


(N, A, B, C) = map(int, input().split())
S = []
for _ in range(N):
    s = input()
    S.append({'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}[s])
solve(A, B, C, S)
