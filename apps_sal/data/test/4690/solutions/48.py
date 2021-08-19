(A, B, C, D) = list(map(int, input().split()))
S1 = A * B
S2 = C * D
if (1 <= A & A <= 10 ** 4) & (1 <= B & B <= 10 ** 4) & (1 <= C & C <= 10 ** 4) & (1 <= D & D <= 10 ** 4):
    if S1 > S2:
        print(S1)
    elif S1 <= S2:
        print(S2)
