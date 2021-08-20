import math
q = int(input())
for i in range(q):
    (x, y, k) = map(int, input().split())
    if x > k or y > k:
        print(-1)
    elif (x + y) % 2 == 0:
        if (k - max(x, y)) % 2 == 0:
            print(k)
        else:
            print(k - 2)
    elif (k - max(x, y)) % 2 == 0:
        print(k - 1)
    else:
        print(k - 1)
