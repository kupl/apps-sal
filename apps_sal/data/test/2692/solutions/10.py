t = int(input())
for i in range(t):
    (n, b) = map(int, input().split())
    x = n // b
    if n % b == 0:
        a = n - x + 1
    else:
        a = n - x
    print(a)
