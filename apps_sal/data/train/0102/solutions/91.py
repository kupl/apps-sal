arr = [11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111]
for t in range(int(input())):
    n = int(int(input()))
    if n < 10:
        res = n
    else:
        res = 9
        for item in arr:
            if n > item*9:
                res += 9
            else:
                res += n // item
                break
    print(res)

