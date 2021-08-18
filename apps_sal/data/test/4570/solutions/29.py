N, A, B = map(int, input().split())
if (1 <= N & N <= 20) & (1 <= A & A <= 100) & (1 <= B & B <= 2000):
    p1 = A * N
    p2 = B
    print(min(p1, p2))
