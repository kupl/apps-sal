N, A, B, C = list(map(int, input().split()))

S = [''] * N
for i in range(N):
    S[i] = input()

result = []
kekka = True


for i in range(N):
    if (A == 0 and B == 0 and S[i] == 'AB') or (C == 0 and B == 0 and S[i] == 'BC') or (A == 0 and C == 0 and S[i] == 'AC'):
        kekka = False
        break
    else:
        if S[i] == 'AB':
            if A == 0:
                A += 1
                B -= 1
                result.append('A')
            elif B == 0:
                A -= 1
                B += 1
                result.append('B')
            elif A == 1 and B == 1 and C == 0 and i != N - 1:
                if S[i + 1] == 'AC':
                    A += 1
                    B -= 1
                    result.append('A')
                else:
                    A -= 1
                    B += 1
                    result.append('B')
            elif A > B:
                A -= 1
                B += 1
                result.append('B')
            else:
                A += 1
                B -= 1
                result.append('A')
        elif S[i] == 'AC':
            if A == 0:
                A += 1
                C -= 1
                result.append('A')
            elif C == 0:
                A -= 1
                C += 1
                result.append('C')
            elif A == 1 and C == 1 and B == 0 and i != N - 1:
                if S[i + 1] == 'AB':
                    A += 1
                    C -= 1
                    result.append('A')
                else:
                    A -= 1
                    C += 1
                    result.append('C')
            elif A > C:
                A -= 1
                C += 1
                result.append('C')
            else:
                A += 1
                C -= 1
                result.append('A')
        else:
            if B == 0:
                B += 1
                C -= 1
                result.append('B')
            elif C == 0:
                B -= 1
                C += 1
                result.append('C')
            elif B == 1 and C == 1 and A == 0 and i != N - 1:
                if S[i + 1] == 'AB':
                    B += 1
                    C -= 1
                    result.append('B')
                else:
                    B -= 1
                    C += 1
                    result.append('C')
            elif B > C:
                B -= 1
                C += 1
                result.append('C')
            else:
                B += 1
                C -= 1
                result.append('B')

if kekka == False:
    print('No')
else:
    print('Yes')
    for i in range(N):
        print((result[i]))
