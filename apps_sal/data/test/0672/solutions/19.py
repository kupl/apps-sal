(a, b) = list(map(int, input().split()))
if a == b:
    print('infinity')
else:
    (k, val) = (1, 0)
    while k * k <= a - b:
        if (a - b) % k == 0:
            val += sum((1 for x in {k, (a - b) // k} if x > b))
        k += 1
    print(val)
