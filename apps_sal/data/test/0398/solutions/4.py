n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n - 2):
    a, b, c = arr[i], arr[i + 1], arr[i + 2]
    if a + b > c:
        print('YES')
        return
print('NO')

