def canoperate(n):
    return str(n)[-1] == '1' and str(n) != '1' or n % 2 == 0


def operate(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n - 1) // 10


(a, b) = map(int, input().split())
res = [b]
while canoperate(b):
    b = operate(b)
    res.append(b)
    if b == a:
        print('YES')
        print(len(res))
        print(*res[::-1])
        break
else:
    print('NO')
