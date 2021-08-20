n = int(input())
A = [int(input()) for _ in range(n)]
sort_A = sorted(A, reverse=True)
for a in A:
    if a == sort_A[0]:
        print(sort_A[1])
    else:
        print(sort_A[0])
