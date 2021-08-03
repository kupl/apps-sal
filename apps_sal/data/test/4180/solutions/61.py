N = int(input())
if N % 1000 == 0:
    print('0')
elif N % 1000 != 0:
    N2 = N // 1000 * 1000 + 1000
    print(N2 - N)
