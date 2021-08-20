N = int(input())
if N == 1:
    print(1)
elif 1 < N < 2 ** 2:
    print(2)
elif 2 ** 2 <= N < 2 ** 3:
    print(4)
elif 2 ** 3 <= N < 2 ** 4:
    print(8)
elif 2 ** 4 <= N < 2 ** 5:
    print(16)
elif 2 ** 5 <= N < 2 ** 6:
    print(32)
elif 2 ** 6 <= N:
    print(64)
