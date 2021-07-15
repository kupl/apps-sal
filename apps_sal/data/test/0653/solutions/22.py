n = int(input())
D = [0] * 10
S = input()
for i in range(len(S)):
    if S[i] in ['L', 'R']:
        if S[i] == 'L':
            for j in range(10):
                if D[j] == 0:
                    D[j] = 1
                    break
        else:
            for j in range(9, -1, -1):
                if D[j] == 0:
                    D[j] = 1
                    break
    else:
        k = int(S[i])
        D[k] = 0

print(''.join(map(str, D)))
