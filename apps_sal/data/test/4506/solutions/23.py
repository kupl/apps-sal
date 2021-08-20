N = int(input())
A = [int(a) for a in input().split()]
B = sorted([int(a) for a in input().split()])[::-1]
AA = []
for i in range(N):
    AA.append(A[i] * (i + 1) * (N - i))
AA = sorted(AA)
print(sum([B[i] * AA[i] for i in range(N)]) % 998244353)
