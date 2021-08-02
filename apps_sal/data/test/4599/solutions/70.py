N = int(input())

A = list(map(int, input().split()))

Alice = 0
Bob = 0

while len(A) != 0:
    Alice += max(A)
    A.remove(max(A))
    if len(A) == 0:
        break
    Bob += max(A)
    A.remove(max(A))
    if len(A) == 0:
        break

print(Alice - Bob)
