(n, m) = list(map(int, input().split()))
if n >= 3 and m >= 3:
    a = n * m
    b = n * 2 + m * 2 - 4
    ans = a - b
elif n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    a = n * m
    b = 2
    ans = a - b
elif n == 2 or m == 2:
    ans = 0
print(ans)
