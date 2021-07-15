N, K = list(map(int, input().split()))
lst = list(range(1, N+1))
for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    lst = list(set(lst) - set(A))
print((len(lst)))

