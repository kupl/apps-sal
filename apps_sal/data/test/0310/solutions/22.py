n, k = list(map(int, input().split()))
if k % n == 0:
    print(k // n)
else:
    print(k // n + 1)
