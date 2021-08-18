
import sys
readline = sys.stdin.readline

K = int(readline())
N = 50

A = [i for i in range(N)]
A = list(map(lambda x: x + (K // N), A))
rest = K % N
for i in range(rest):
    A[i] += N
    for j in range(N):
        if i != j:
            A[j] -= 1

print(N)
print(*A)
