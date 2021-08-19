import sys
input = sys.stdin.readline
n, a, b = map(int, input().split())
nn = n
bb = b

if (n + b - 1) // b <= a <= n + 1 - b:
    ANS = []
    L = [a]
    b -= 1
    n -= a
    for i in range(b):
        L.append(1)
        n -= 1
    ind = 1
    while n > 0:
        p = min(n, a - 1)
        L[ind] += p
        n -= p
        ind += 1

    # print(L)

    i = nn
    for j in range(bb):
        i -= L[j]
        for k in range(L[j]):
            ANS.append(i + k + 1)

    print(*ANS)
else:
    print(-1)
