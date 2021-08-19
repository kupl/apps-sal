N = int(input())
A = [int(T) for T in input().split()]
Min = 10 ** 9
for TN in range(min(A), max(A) + 1):
    Min = min(Min, sum(((TN - TA) ** 2 for TA in A)))
print(Min)
