(n, k) = list(map(int, input().split()))
k -= 1
x = 1
while True:
    if k % 2 ** x == 2 ** (x - 1) - 1:
        print(x)
        break
    x += 1
