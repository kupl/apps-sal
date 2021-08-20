N = int(input())
if N % 2 == 0:
    print(float(1 / 2))
else:
    print(float(1 - (N - 1) / 2 / N))
