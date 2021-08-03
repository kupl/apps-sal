N, X = map(int, input().split())
sweet = [0] * N
for l in range(N):
    sweet[l] = int(input())
S = sum(sweet)
R = X - S
A = min(sweet)
C = R // A
print(N + C)
