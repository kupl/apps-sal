A = input()
print(sum(i != j for i, j in zip(A, A[::-1])) // 2)
