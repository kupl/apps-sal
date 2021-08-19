# A
# A = list(map(int, input().split()))

N = int(input())
A = list(map(int, input().split()))
SUM = 0
SUM_A = sum(A)
for i in range(len(A)):
    SUM += A[i]
    if SUM >= SUM_A / 2:
        print(i + 1)
        quit()
