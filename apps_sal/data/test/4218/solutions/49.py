N = int(input())
if N % 2 == 0:
    print(0.5)
else:
    X = N // 2
    print(1 - X / N)
