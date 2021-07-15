n, k = map(int, input().strip().split(' '))

if k % n == 0:
    print(k // n)
else:
    print(k // n + 1)
