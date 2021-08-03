N = int(input())
testimony = []
for i in range(N):
    A = int(input())
    testimony.append([-1] * N)
    for i in range(A):
        x, y = map(int, input().split())
        testimony[-1][x - 1] = y

ans = 0
for i in range(2**N):
    total = 0
    tmplst = [0] * N
    for j in range(N):
        if ((i >> j) & 1):
            tmplst[j] = 1

    ch = 0
    for j in range(N):
        if tmplst[j] == 1:
            for a, b in zip(testimony[j], tmplst):
                if (a == 1 and b == 0) or (a == 0 and b == 1):
                    ch = 1
                    break

            if ch == 1:
                break

    if ch == 0:
        if ans < sum(tmplst):
            ans = sum(tmplst)

print(ans)
