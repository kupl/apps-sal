n, a = list(map(int, input().split()))
k = a % 2
i = 1
if k == 0:
    na = n
    while na != a:
        na = na - 2
        i += 1
else:
    na = 1
    while a != na:
        na += 2
        i += 1
print(i)
