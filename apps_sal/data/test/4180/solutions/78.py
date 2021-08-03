N = input()
N = int(N)

for X in range(0, 11):
    a = N - 1000 * X

    if a <= 0:
        break
C = 1000 * (X) - N
print(C)
