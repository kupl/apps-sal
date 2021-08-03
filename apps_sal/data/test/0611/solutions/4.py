n, m = list(map(int, input().split()))
ans = 0
num1 = n // 2
num2 = n // 2
num3 = n * (n - 1) // 2
if n % 2 == 0:
    num1 -= 1

num1 = (num1 + 1) * num1 // 2
num2 = (num2 + 1) * num2 // 2

while m > 0:
    x, d = list(map(int, input().split()))
    ans += x * n
    if d < 0:
        ans += d * num1
        ans += d * num2
    else:
        ans += d * num3
    m -= 1

print(ans / n)
