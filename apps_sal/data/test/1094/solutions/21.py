n = int(input())
A = [0] * n
for i in range(n):
    A[i] = input()
mass = set()
per = 0
for i in range(n - 1, -1, -1):
    mass.add(A[i])
    t = len(mass)
    if t > per:
        per = t
        print(A[i])
