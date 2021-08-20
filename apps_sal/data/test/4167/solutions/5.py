(n, k) = list(map(int, input().split()))
n_O = 0
n_E = 0
for i in range(1, n + 1):
    if 2 * i % k == 0:
        if 2 * i // k % 2 == 0:
            n_E += 1
        else:
            n_O += 1
print(n_E ** 3 + n_O ** 3)
