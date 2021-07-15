import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
for i in range(n):
    d = 0
    while A[i] > 0:
        if A[i] % 2 == 0:
            d += 1
            A[i] = A[i] // 2
        else:
            break
    A[i] = d
print(sum(A))
