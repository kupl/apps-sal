def dl(n):
    ret = 0
    i = 1
    while (i * i <= n):
        if (n % i == 0):
            ret = i
        i += 1
    return ret


n = int(input())
kek1 = dl(n)
kek2 = n // kek1
print(kek1, kek2)
