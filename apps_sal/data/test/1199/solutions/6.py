n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
mit = 1
col = 1
for i in range(1, m + 1):
    t = arr.count(i)
    if t > col:
        mit = i
        col = t
print(n - max(0, col - (n - col)))
for i in range(n):
    print(arr[(i + col) % n], arr[i])
