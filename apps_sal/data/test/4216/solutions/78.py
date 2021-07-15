
N = int(input())
F = [100000000000, 1]

for a in range(1, int(N ** 0.5) + 1):
    if N % a == 0:
        b = int(N / a)
        f = [a, b]
        if max(len(str(f[0])), len(str(f[1]))) < max(len(str(F[0])), len(str(F[1]))):
            F = f

print(max(len(str(F[0])), len(str(F[1]))))
