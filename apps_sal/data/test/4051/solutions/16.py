n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    if abs(arr[i] - arr[i + 1]) >= 2:
        print('NO')
        break
else:
    print('YES')

