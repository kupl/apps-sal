(n, a, b) = map(int, input().split())
one = 0
our = list(map(int, input().split()))
res = 0
for elem in our:
    if elem == 2:
        if b > 0:
            b -= 1
        else:
            res += 2
    elif a > 0:
        a -= 1
    elif b > 0:
        b -= 1
        one += 1
    elif one > 0:
        one -= 1
    else:
        res += 1
print(res)
