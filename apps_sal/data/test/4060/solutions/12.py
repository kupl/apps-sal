n = int(input())
s = input()

def sol(n, S):
    L = [0]
    for s in S:
        if s == "(":
            L.append(L[-1] + 1)
        else:
            L.append(L[-1] - 1)
    ANS = 0
    L = L[1:]
    if L[-1] == 2:
        if min(L) < 0:
            return 0
        for j in range(n-1, -1, -1):
            if L[j] < 2:
                break
        for k in range(j+1, n, 1):
            if S[k] == '(':
                ANS += 1
    elif L[-1] == -2:
        if min(L) < -2:
            return 0
        for j in range(n):
            if L[j] < 0:
                break
        for k in range(j, -1, -1):
            if S[k] == ')':
                ANS += 1
    else:
        ANS = 0
    return ANS

print(sol(n, s))
