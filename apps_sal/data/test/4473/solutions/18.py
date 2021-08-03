t = int(input())
for i in range(t):
    a, b, k = list(map(int, input().split()))
    ak = (k + 1) // 2
    bk = k - ak
    print(ak * a - bk * b)
