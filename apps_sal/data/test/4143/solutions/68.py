from math import ceil
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
a = ceil(N / A)
F = [A, B, C, D, E]
for i in range(1, 5):
    if F[i - 1] <= F[i]:
        a += 1
    else:
        b = ceil(N / F[i])
        a = max(a + 1, b + i)
print(a)
