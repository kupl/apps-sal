import math
n = int(input())
list_ = list(map(int, input().split()))
if 1 in list_:
    print(n - list_.count(1))
else:
    result = n + 1
    for i in range(n):
        cnt = 0
        gcd = list_[i]
        for j in range(n - i):
            gcd = math.gcd(gcd, list_[i + j])
            if gcd == 1:
                result = min(result, cnt)
            cnt += 1
    if result == n + 1:
        print(-1)
    else:
        print(result + n - 1)
