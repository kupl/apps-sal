N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] * (N + 1)
S = set()
for i in range(N, 0, -1):
    if sum(B[i::i]) % 2 != A[i]:
        B[i] = 1
        S.add(i)
print(len(S))
print(*S)
