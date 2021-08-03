from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [(e, e) for e in arr]
    res = []
    while len(arr) > 0:
        arr.sort()
        x = arr.pop()
        res.append(x[1])
        for i in range(len(arr)):
            arr[i] = (gcd(arr[i][0], x[0]), arr[i][1])
    print(*res)
