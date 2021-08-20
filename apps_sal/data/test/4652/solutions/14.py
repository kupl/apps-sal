import math
q = int(input())
for i in range(q):
    n = int(input())
    arr = input().split()
    for i in range(n):
        arr[i] = int(arr[i])
    if n <= 3:
        print('YES')
    else:
        havent = True
        val = (arr[1] - arr[0]) % n
        if val != 1 and val != n - 1:
            print('NO')
        else:
            for i in range(n - 1):
                if (arr[i + 1] - arr[i]) % n != val and havent:
                    print('NO')
                    havent = False
            if havent:
                print('YES')
