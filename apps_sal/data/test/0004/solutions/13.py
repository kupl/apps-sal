x = int(input())
n, m = list(map(int, input().split()))
a = 0
while (n % 10 != 7 and n // 10 != 7 and m % 10 != 7 and m // 10 != 7):
    m -= x
    if m < 0:
        m += 60
        n -= 1
        if n < 0:
            n  += 24
    a += 1
print(a)

