N, L = map(int, input().split())

La = N * L + (N - 1) * N / 2

min_Le = La
abs_L = int(1e100)
for i in range(N):
    Li = L + (i + 1) - 1
    if abs((La - Li) - La) < abs_L:
        Le = La - Li
        abs_L = abs(Le - La)

print(int(Le))
