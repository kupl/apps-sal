(N, M) = map(int, input().split())
A = [int(i) for i in range(N)]
B = []
if N % 2 == 0:
    center = N // 2
    c1 = center // 2
    c2 = center + c1
    for i in range(1, M + 1):
        j = i // 2
        if i % 2 == 1:
            B.append((c1 - j, c1 + j + 1))
        else:
            B.append((c2 - (j - 1), c2 - (j - 1) + 2 * j))
else:
    center = N // 2 + 1
    for i in range(1, M + 1):
        B.append((center - i, center + i))
for i in B:
    print(i[0], i[1])
