t = int(input())
for i in range(t):
    (n, b) = list(map(int, input().split()))
    q = n // b
    if n % b == 0:
        a = n - q + 1
    else:
        a = n - q
    print(a)
