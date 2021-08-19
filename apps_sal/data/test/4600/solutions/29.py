(N, M) = map(int, input().split())
AC = [0] * N
WA1 = [0] * N
WA2 = [0] * N
for i in range(M):
    (p, s) = input().split()
    if s == 'AC':
        if AC[int(p) - 1] == 0:
            AC[int(p) - 1] = 1
            WA2[int(p) - 1] = WA1[int(p) - 1]
    elif AC[int(p) - 1] == 0:
        WA1[int(p) - 1] += 1
print(str(AC.count(1)) + ' ' + str(sum(WA2)))
