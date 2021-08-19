n = int(input())
a = [1] * n
ans = 1
for i in range(1, n + 1):
    b = 2
    while i != 1:
        if i % b == 0:
            i //= b
            a[b - 1] += 1
        else:
            b += 1
for i in a:
    if 1 < i:
        ans *= i
        ans %= 10 ** 9 + 7
print(ans)
