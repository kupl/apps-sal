R = lambda: map(int, input().split())
n, k = R()
arr = [i + 1 for i in range(n * 2)]
for i in range(0, 2 * k, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(' '.join(map(str, arr)))
