A=input();print(sum([A[i]!=A[::-1][i] for i in range(len(A))])//2)
