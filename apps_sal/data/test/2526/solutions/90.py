X, Y, A, B, C = map(int, input().split())
*P, = sorted(map(int, input().split()))
*Q, = sorted(map(int, input().split()))
*R, = map(int, input().split())

P = P[-X:]
Q = Q[-Y:]
R = sorted(P + Q + R)
ans = sum(R[-(X + Y):])
print(ans)
