n, m = map(int, input().split())
i = 1
while i ** 2 <= m:
    if m % i == 0:
        if i + m // i == n:
            print("Yes")
            return
    i += 1
print("No")
