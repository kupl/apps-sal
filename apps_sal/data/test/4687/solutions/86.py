n, k = map(int, (input().split()))
arr = [0] * 100100
for i in range(n):
    a, b = map(int, input().split())
    arr[a] += b

cur = 0
for i in range(100100):
    cur += arr[i]
    if cur >= k:
        print(i)
        break
