N, M = list(map(int, input().split()))

if N < 2:
    guusuu = 0
else:
    guusuu = N * (N - 1) / 2

if M < 2:
    kisuu = 0
else:
    kisuu = M * (M - 1) / 2

print(int(guusuu + kisuu))
