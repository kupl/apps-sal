import copy
n = int(input())
T = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    A = copy.copy(T)
    (a, b) = map(int, input().split())
    A[a - 1] = b
    print(sum(A))
