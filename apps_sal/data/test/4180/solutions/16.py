N = int(input())

if N % 1000 == 0:
    print((0))
else:
    print(((N // 1000 + 1) * 1000 - N))
