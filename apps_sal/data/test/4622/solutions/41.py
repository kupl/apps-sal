N = int(input())
A = list(map(int, input().split()))
A.sort()
print('YNEOS'[any((a == b for (a, b) in zip(A, A[1:])))::2])
