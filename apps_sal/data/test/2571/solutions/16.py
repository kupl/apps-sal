t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    keys = []
    for i in range(len(arr)):
        keys.append(arr[-(i + 1)] * (-1 if i % 2 == 0 else 1))
    print(*keys)
