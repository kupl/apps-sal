def gcd(a, b):
    return (a if b == 0 else gcd(b, a % b))


def nk(a, b):
    return (a * b) // gcd(a, b)


def check(arr, x, y, a, b, mid, k):
    GdCN = mid // nk(a, b)
    if x > y:
        MAP = x
        MIP = y
        MAD = a
        MID = b
    else:
        MAP = y
        MIP = x
        MAD = b
        MID = a
    GCN = mid // MAD - GdCN
    BCN = mid // MID - GdCN
    #print(arr[:GdCN], arr[GdCN:GdCN + GCN], arr[GdCN + GCN:GdCN + GCN + BCN])
    #print(mid, GdCN, GCN, BCN, sum(arr[:GdCN]) * ((x + y) // 100) + sum(arr[GdCN:GdCN + GCN]) * (MAP // 100) + sum(arr[GdCN + GCN:GdCN + GCN + BCN]) * (MIP // 100))
    if sum(arr[:GdCN]) * (x + y) // 100 + sum(arr[GdCN:GdCN + GCN]) * MAP // 100 + sum(arr[GdCN + GCN:GdCN + GCN + BCN]) * MIP // 100 >= k:
        return True
    else:
        return False


n = int(input())
for i in range(n):
    input()
    arr = [int(x) for x in input().split()]
    x, a = [int(x) for x in input().split()]
    y, b = [int(x) for x in input().split()]
    k = int(input())
    arr = sorted(arr)[::-1]
    left = 0
    right = len(arr)
    while right - left > 1:
        mid = (right + left) // 2
        if check(arr, x, y, a, b, mid, k):
            right = mid
        else:
            left = mid
    if check(arr, x, y, a, b, left, k):
        print(left)
    elif check(arr, x, y, a, b, right, k):
        print(right)
    else:
        print(-1)
    # print('--------------------------------------------------')
