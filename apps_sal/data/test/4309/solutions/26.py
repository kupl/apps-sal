N = int(input())
if N % 111:
    print(111 * (N // 111 + 1))
else:
    print(111 * int(N / 111))
