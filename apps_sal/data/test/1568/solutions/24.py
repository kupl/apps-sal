n, a, b, c, t = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]
ret = 0

if b < c:
    for i in array:
        ret += c * (t - i) + a - (t - i) * b
    print(ret)

else:
    print(n * a)
