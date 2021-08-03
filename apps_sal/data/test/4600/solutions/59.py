N, M = map(int, input().split())

AC = [0] * N
WA = [0] * N

for _ in range(M):
    p, S = input().split()
    p = int(p) - 1
    if AC[p] == 1:
        continue
    else:
        if S == 'AC':
            AC[p] = 1
        else:
            WA[p] += 1

Pen = [x * y for (x, y) in zip(AC, WA)]

print(sum(AC), sum(Pen))
