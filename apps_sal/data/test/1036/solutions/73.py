(N, K) = map(int, input().split())
S = input()
prev = [S[i % N] for i in range(2 * N)]
for i in range(K):
    res = []
    for j in range(N):
        if prev[j * 2] == 'R':
            if prev[j * 2 + 1] == 'R':
                res.append('R')
            elif prev[j * 2 + 1] == 'P':
                res.append('P')
            else:
                res.append('R')
        elif prev[j * 2] == 'P':
            if prev[j * 2 + 1] == 'R':
                res.append('P')
            elif prev[j * 2 + 1] == 'P':
                res.append('P')
            else:
                res.append('S')
        elif prev[j * 2 + 1] == 'R':
            res.append('R')
        elif prev[j * 2 + 1] == 'P':
            res.append('S')
        else:
            res.append('S')
    prev = res + res
print(res[0])
