(N, M) = [int(a) for a in input().split()]
a1 = min(N, M // 2)
a2 = 0
if M // 2 > N:
    a2 = (M - N * 2) // 4
a3 = a1 + a2
print(a3)
