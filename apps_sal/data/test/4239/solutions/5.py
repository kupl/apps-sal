N = int(input())
A = [1, 6, 36, 6 ** 3, 6 ** 4, 6 ** 5, 6 ** 6, 9, 81, 9 ** 3, 9 ** 4, 9 ** 5]
B = [0] + [N] * N
i = 0
while i <= N:
    for a in A:
        if a + i <= N:
            B[a + i] = min(B[a + i], B[i] + 1)
    i += 1
print(B[N])
