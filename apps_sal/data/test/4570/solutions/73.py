# A - Parking
# N A B

N, A, B = list(map(int, input().split()))

# A * N < B ⇔ B

if (N * A) < B:
    print((N * A))
else:
    print(B)
