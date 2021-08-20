n = int(input())
A = [1]
B = []
for _ in range(n):
    new_A = [0] + A[:]
    new_B = A[:]
    for (i, b) in enumerate(B):
        new_A[i] += b
    A = [a % 2 for a in new_A]
    B = [b % 2 for b in new_B]
print(len(A) - 1)
print(*A)
print(len(B) - 1)
print(*B)
