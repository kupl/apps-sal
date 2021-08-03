n = int(input())

x1, x2 = list(map(float, input().split()))

arr = []

for i in range(n):
    p, q = list(map(float, input().split()))
    r1 = p * x1 + q
    r2 = p * x2 + q
    arr.append((r1, r2))

arr = sorted(arr)

flag = False

for i in range(n - 1):
    if arr[i][0] < arr[i + 1][0] and arr[i][1] > arr[i + 1][1]:
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')
