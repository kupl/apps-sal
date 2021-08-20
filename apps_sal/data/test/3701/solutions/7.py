(n, x, y) = map(int, input().split())
a = input()
if '0' not in a:
    print(0)
else:
    number_of_zero_groups = 0
    curr = a[0]
    if curr == '0':
        number_of_zero_groups += 1
    for e in a[1:]:
        if e == '0' and curr == '1':
            number_of_zero_groups += 1
        curr = e
    print((number_of_zero_groups - 1) * min(x, y) + y)
