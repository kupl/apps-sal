n = int(input())


ans = 0
tmp = 0
p = 1
if n % 2 == 0:
    k = n // 2
    while True:
        tmp = k // pow(5, p)

        ans += tmp
        p += 1

        if tmp == 0:
            break

print(ans)
