def f(N, L):
    V = [0] * (N + 1)
    for i, a in enumerate(L):
        if V[a] > 0:
            r = V[a]
            if L[i - 1] == a:
                r -= 1
            if r > 0:
                return True
        V[a] += 1
    return False


for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    if f(N, L): print('YES')
    else: print('NO')
