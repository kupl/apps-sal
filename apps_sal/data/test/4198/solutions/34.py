(A, B, X) = map(int, input().split())
N = 10 ** 9
(low, high) = (0, N + 1)
while low + 1 < high:
    mid = (low + high) // 2
    if A * mid + B * len(str(mid)) <= X:
        low = mid
    else:
        high = mid
print(low)
