n = int(input())
arr = list(map(int, input().split()))
if sum(arr) % 200 == 0 and arr.count(100) > 0 or sum(arr) % 400 == 0:
    print('YES')
else:
    print('NO')
