N = int(input())
A = list(map(int, input().split()))

A_set = set(A)
eat = len(A) - len(A_set)
if eat % 2 == 0:
    print(len(A_set))
else:
    print(len(A_set) - 1)
