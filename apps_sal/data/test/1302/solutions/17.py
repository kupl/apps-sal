(n, k) = map(int, input().split())
array = [0] + [i + 1 for i in range(n)]
if n == k:
    print(-1)
else:
    for i in range(0, n - k - 1):
        (array[1], array[n - i]) = (array[n - i], array[1])
    print(*array[1:])
