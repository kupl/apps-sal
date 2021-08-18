A, B, C = map(int, input().split())
if (1 <= A & A <= 100) & (1 <= B & B <= 100) & (1 <= C & C <= 100):
    C_price = A * C
    if B < C_price:
        B_count = int(B / A)
    elif B >= C_price:
        B_count = C
    print(B_count)
