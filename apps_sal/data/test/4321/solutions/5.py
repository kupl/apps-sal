(x, k) = map(int, input().split())
while k != 0:
    if x % 10 == 0:
        x /= 10
    else:
        x -= 1
    k -= 1
print(int(x))
