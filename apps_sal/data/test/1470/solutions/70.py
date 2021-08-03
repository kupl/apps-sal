N = int(input())
if N % 11 == 0:
    print(N // 11 * 2)
elif N % 11 <= 6:
    print(N // 11 * 2 + 1)
else:
    print(N // 11 * 2 + 2)
