n = int(input())
A = list(map(int, input().split()))
C = [0] * n
for i in range(n):
    cnt = 0
    while A[i] % 2 == 0:
        cnt += 1
        A[i] //= 2
    C[i] = cnt
print(sum(C))
