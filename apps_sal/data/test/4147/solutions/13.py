n, a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]


def check(t):
    ca = t.count('a')
    cb = t.count('b')
    cc = t.count('c')
    if ca == 0 or cb == 0 or cc == 0:
        return False
    return True


def calc(t):
    A, B, C = 0, 0, 0
    d = (t.count('a') - 1 + t.count('b') - 1 + t.count('c') - 1) * 10
    for i, j in enumerate(t):
        if j == 'a':
            A += l[i]
        elif j == 'b':
            B += l[i]
        elif j == 'c':
            C += l[i]
    d += abs(A - a) + abs(B - b) + abs(C - c)
    return d


ary = ['a', 'b', 'c', 'd']
take = []


def dfs(s):
    if len(s) == n:
        if check(s):
            take.append(calc(s))
        return
    for i in range(4):
        dfs(s + ary[i])


dfs('')

print(min(take))
