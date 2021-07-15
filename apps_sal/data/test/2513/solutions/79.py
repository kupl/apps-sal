import sys
N = int(input())
S = input()

X = [''] * (N + 1)
X[0] = 'S'
X[1] = 'S'
for i in range(1, N):
    if X[i] == 'S':
        if S[i] == 'o':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
    else:
        if S[i] == 'x':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
if X[-1] == 'S':
    if (X[-2] == 'S' and S[0] == 'o') or (X[-2] == 'W' and S[0] == 'x'):
        X.pop()
        for x in X:
            print(x, end='')
        print('')
        return

X = [''] * (N + 1)
X[0] = 'S'
X[1] = 'W'
for i in range(1, N):
    if X[i] == 'S':
        if S[i] == 'o':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
    else:
        if S[i] == 'x':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
if X[-1] == 'S':
    if (X[-2] == 'S' and S[0] == 'x') or (X[-2] == 'W' and S[0] == 'o'):
        X.pop()
        for x in X:
            print(x, end='')
        print('')
        return

X = [''] * (N + 1)
X[0] = 'W'
X[1] = 'S'
for i in range(1, N):
    if X[i] == 'S':
        if S[i] == 'o':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
    else:
        if S[i] == 'x':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
if X[-1] == 'W':
    if (X[-2] == 'S' and S[0] == 'x') or (X[-2] == 'W' and S[0] == 'o'):
        X.pop()
        for x in X:
            print(x, end='')
        print('')
        return

X = [''] * (N + 1)
X[0] = 'W'
X[1] = 'W'
for i in range(1, N):
    if X[i] == 'S':
        if S[i] == 'o':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
    else:
        if S[i] == 'x':
            X[i + 1] = X[i - 1]
        else:
            if X[i - 1] == 'S':
                X[i + 1] = 'W'
            else:
                X[i + 1] = 'S'
if X[-1] == 'W':
    if (X[-2] == 'S' and S[0] == 'o') or (X[-2] == 'W' and S[0] == 'x'):
        X.pop()
        for x in X:
            print(x, end='')
        print('')
        return

print('-1')
