x = int(input())
n = x + (x - 1) % 2
ans = 0

found = True

while found:
    found = False
    if x == 2:
        ans = x
        break

    for i in range(3, n // 2, 2):
        if n % i == 0:
            found = True
            break
    ans = n
    n += 2
print(ans)
