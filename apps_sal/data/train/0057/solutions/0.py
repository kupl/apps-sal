t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[-1] > arr[0]:
        print('YES')
    else:
        print('NO')
