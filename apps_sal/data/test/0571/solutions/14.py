def fix(S):
    N = len(S)
    s = 0
    minS = 0
    for n in range(N):
        if S[n] == '(':
            s += 1
        elif S[n] == ')':
            s -= 1
        minS = min(minS, s)
    if minS < 0:
        for n in range(N):
            if S[n] == '?':
                S[n] = '('
                minS += 1
                s += 1
                if not minS:
                    break
    if s > 0:
        for n in range(N - 1, -1, -1):
            if S[n] == '?':
                S[n] = ')'
                s -= 1
                if not s:
                    break
    nq = 0
    for n in range(N):
        if S[n] == '?':
            nq += 1
    if nq % 2:
        return False
    added = 0
    for n in range(N):
        if S[n] == '?':
            if added < nq // 2:
                S[n] = '('
            else:
                S[n] = ')'
            added += 1
    s = 0
    for n in range(N):
        if S[n] == '(':
            s += 1
        else:
            s -= 1
        if s < 0:
            return False
    if s:
        return False
    return S


def sv():
    N = int(input())
    S = list(input())
    if N % 2:
        return False
    if S[0] == ')' or S[N - 1] == '(':
        return False
    if N == 2:
        print('()')
        return True
    f = fix(S[1:-1])
    if not f:
        return False
    print('(%s)' % ''.join(f))
    return True


if not sv():
    print(':(')
