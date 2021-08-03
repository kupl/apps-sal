N = int(input())
A = sorted(list(map(int, input().split())))

if N % 2 == 0:
    B = [1 + 2 * (n // 2) for n in range(N)]
else:
    B = [2 * (n // 2) for n in range(1, 1 + N)]

if A == B:
    print(pow(2, N // 2, 10**9 + 7))
else:
    print(0)
