N = int(input())
C = sorted(list(map(int, input().split())), reverse=True)
L = 10 ** 9 + 7
if N > 1:
    b = 2 ** (N - 2) % L
    a = [C[i] * b * (2 + i) % L for i in range(N)]
    print(sum(a) * b * 2 * 2 % L)
else:
    print(C[0] * 2 % L)
