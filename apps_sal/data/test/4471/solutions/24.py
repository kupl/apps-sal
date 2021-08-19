t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    arr = list(map(int, input().split()))
    mn = min(arr)
    for el in arr:
        s += (el - mn) % 2
    if s == 0:
        print('YES')
    else:
        print('NO')
