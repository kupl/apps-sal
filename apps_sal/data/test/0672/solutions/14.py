tmp = input().split()
a = int(tmp[0])
b = int(tmp[1])
a -= b
if a == 0:
    print('infinity')
else:
    ans = 0
    i = 1
    while i * i < a:
        if a % i == 0:
            if i > b:
                ans += 1
            if a / i > b:
                ans += 1
        i += 1
    if i * i == a and i > b:
        ans += 1
    print(ans)
