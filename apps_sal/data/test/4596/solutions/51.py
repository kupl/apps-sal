n = int(input())
A = [0] * n
L = list(map(int, input().split()))
for i in range(n):
    cnt = 0
    while L[i] % 2 == 0:
        L[i] = L[i] / 2
        cnt += 1
    A[i] = cnt
print(min(A))
