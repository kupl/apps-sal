n, a, b, c, d = list(map(int, input().split()))
arr = [0] * 4
arr[0] = a + b
arr[1] = a + c
arr[2] = c + d
arr[3] = b + d
arr.sort()
if n + arr[0] - arr[3] >= 0:
    print(n * (n + arr[0] - arr[3]))
else:
    print(0)
