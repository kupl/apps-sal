(n, s) = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort()
if sum(arr[:-1]) <= s:
    print('YES')
else:
    print('NO')
