N = int(input())

A = list(map(int, input().split()))

if A[0] == 0:
    B = [1, -1]
    ANS = [1, 1]
else:
    B = [A[0], (-1) * (A[0]) // abs(A[0])]
    ANS = [0, abs(A[0]) + 1]

for i in range(len(B)):
    b = B[i]
    for a in A[1:]:
        if a + b == 0:
            ANS[i] += 1
            b = (-1) * (b) // abs(b)
        elif b * (a + b) < 0:
            b += a
        else:
            ANS[i] += abs(a + b) + 1
            b = (-1) * (a + b) // abs(a + b)
print(min(ANS))
