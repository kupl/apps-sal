A, B, N = [int(x) for x in input().split()]

Q = A // B
R = A % B

if R == 0:
    ans = Q * (B - 1)
elif B <= N:
    ans = R - 1 + Q * (B - 1)
else:
    ans = int(A * N / B) - A * int(N / B)

print(ans)
