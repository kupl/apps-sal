(N, M) = map(int, input().split())
(K, *result) = map(int, input().split())
result = set(result)
for _ in range(N - 1):
    (K, *A) = map(int, input().split())
    A = set(A)
    result = result & A
print(len(result))
