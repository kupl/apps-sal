N, A, B, C = map(int, input().split())
l = []
i = 0
j = 0

if A + B + C != 2:
    pass
else:
    s = []
    while i < N:
        s.append(input())
        i += 1
    if (A == 2 and s[0] == 'BC') or (B == 2 and s[0] == 'AC') or (C == 2 and s[0] == 'AB'):
        print('No')
        return
    print('Yes')
    while j < N:
        if j < N and s[j] == 'AB':
            if A == B == 1:
                if j == N - 1:
                    print('A')
                    return
                if j < N - 1 and s[j + 1] == 'AB':
                    A = 2
                    B = 0
                    print('A')
                elif s[j + 1] == 'BC':
                    A = 0
                    B = 1
                    C = 1
                    print('B\nC')
                    j += 1
                else:
                    A = 1
                    B = 0
                    C = 1
                    print('A\nC')
                    j += 1
            else:
                if A > B:
                    print('B')
                    A -= 1
                    B += 1
                else:
                    print('A')
                    A += 1
                    B -= 1
            j += 1
        if j < N and s[j] == 'BC':
            if B == C == 1:
                if j == N - 1:
                    print('B')
                    return
                if j < N - 1 and s[j + 1] == 'BC':
                    B = 2
                    C = 0
                    print('B')
                elif s[j + 1] == 'AB':
                    A = 1
                    B = 1
                    C = 0
                    print('B\nA')
                    j += 1
                else:
                    A = 1
                    B = 0
                    C = 1
                    print('C\nA')
                    j += 1
            else:
                if B > C:
                    print('C')
                    B -= 1
                    C += 1
                else:
                    print('B')
                    B += 1
                    C -= 1
            j += 1
        if j < N and s[j] == 'AC':
            if A == C == 1:
                if j == N - 1:
                    print('A')
                    return
                if j < N - 1 and s[j + 1] == 'AC':
                    A = 2
                    C = 0
                    print('A')
                elif s[j + 1] == 'AB':
                    A = 1
                    B = 1
                    C = 0
                    print('A\nB')
                    j += 1
                else:
                    A = 0
                    B = 1
                    C = 1
                    print('C\nB')
                    j += 1
            else:
                if A > C:
                    print('C')
                    A -= 1
                    C += 1
                else:
                    print('A')
                    A += 1
                    C -= 1
            j += 1
if A + B + C == 2:
    return

for i in range(N):
    s = input()
    if s == 'AB':
        if A > B:
            A -= 1
            B += 1
            l.append('B')
        else:
            A += 1
            B -= 1
            l.append('A')
    if s == 'BC':
        if B > C:
            B -= 1
            C += 1
            l.append('C')
        else:
            B += 1
            C -= 1
            l.append('B')
    if s == 'AC':
        if C > A:
            C -= 1
            A += 1
            l.append('A')
        else:
            C += 1
            A -= 1
            l.append('C')
    if A < 0 or B < 0 or C < 0:
        print('No')
        return
print('Yes')
print(*l, sep='\n')
