A, B, K = map(int, input().split())
S = []

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        S.append(i)

print(S[-K])
