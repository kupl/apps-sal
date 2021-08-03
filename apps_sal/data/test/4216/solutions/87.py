N = int(input())
A = 1
for i in range(2, int(N**(1 / 2)) + 1):
    if N % i == 0:
        A = i
B = str(N // A)
A = str(A)
print(max(len(B), len(A)))
