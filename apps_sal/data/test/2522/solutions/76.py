N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [(a, i, 0) for i, a in enumerate(A)] + [(b, i, 1) for i, b in enumerate(B)]
AB.sort()

X = AB[:N]
Y = AB[N:]

if any(x[0] == y[0] for x, y in zip(X, Y)):
    print('No')
    return

swapA = []
swapB = []
ans = [-1] * N

for (_, i, sx), (_, j, sy) in zip(X, Y):
    if sx == sy == 0:
        swapA.append((i, j))
    elif sx == sy == 1:
        swapB.append((i, j))
    else:
        if sx == 0:
            ans[i] = B[j]
        else:
            ans[j] = B[i]

for (i, j), (x, y) in zip(swapA, swapB):
    ans[i] = B[x]
    ans[j] = B[y]

    if A[i] == ans[i] or A[j] == ans[j]:
        ans[i], ans[j] = ans[j], ans[i]

print('Yes')
print((*ans))
