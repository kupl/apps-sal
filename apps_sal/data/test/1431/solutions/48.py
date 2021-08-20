N = int(input())
A = list(map(int, input().split()))
A = [0] + A
B = [0] * (N + 1)
for i in range(N):
    k = N - i
    c = 0
    for j in range(k, N + 1, k):
        c += B[j]
        c %= 2
    if A[k] != c:
        B[k] = 1
print(sum(B))
for i in range(len(B)):
    if B[i] == 1:
        print(i)
