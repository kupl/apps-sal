N = int(input())

Fs = [len(str(N))]

for n in range(2, int(N ** (1 / 2)) + 1):
    if N % n == 0:
        num_digit = len(str(n)) if len(str(n)) >= len(str(N // n)) else len(str(N // n))
        Fs.append(num_digit)

print(min(Fs))
