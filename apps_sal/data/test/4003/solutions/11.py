import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
LIST = [1] * n
LIST_INV = [1] * n
for i in range(n - 2, -1, -1):
    if A[i] < A[i + 1]:
        LIST[i] = LIST[i + 1] + 1
for i in range(1, n):
    if A[i] < A[i - 1]:
        LIST_INV[i] = LIST_INV[i - 1] + 1
ANS = []
SCORE = 0
i = 0
j = n - 1
while True:
    if i == j and A[i] > SCORE:
        ANS.append('R')
        SCORE = A[i]
        break
    if A[i] > A[j] and A[j] > SCORE:
        ANS.append('R')
        SCORE = A[j]
        j -= 1
    elif A[i] < A[j] and A[i] > SCORE:
        ANS.append('L')
        SCORE = A[i]
        i += 1
    elif A[i] > A[j] and A[j] <= SCORE and (A[i] > SCORE):
        ANS.append('L')
        SCORE = A[i]
        i += 1
    elif A[i] < A[j] and A[i] <= SCORE and (A[j] > SCORE):
        ANS.append('R')
        SCORE = A[j]
        j -= 1
    elif A[i] == A[j] and A[i] > SCORE:
        if LIST[i] > LIST_INV[j]:
            ANS.append('L')
            SCORE = A[i]
            i += 1
        else:
            ANS.append('R')
            SCORE = A[j]
            j -= 1
    else:
        break
print(len(ANS))
print(''.join(ANS))
