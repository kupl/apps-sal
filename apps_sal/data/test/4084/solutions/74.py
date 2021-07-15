N, A, B = list(map(int, input().split()))
C = int(N/(A+B))
D = N%(A+B)
ans = 0
if 0 <= D <= A:
    ans = A*C + D
else:
    ans = A*C + A

print(ans)

