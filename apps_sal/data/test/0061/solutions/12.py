def convert(digits, base):
    res = 0
    digits.reverse()
    power = 1
    for i in digits:
        res += i * power
        power *= base
    return res


(n, base_a) = [int(x) for x in input().split()]
digits_a = [int(x) for x in input().split()]
a = convert(digits_a, base_a)
(n, base_a) = [int(x) for x in input().split()]
digits_a = [int(x) for x in input().split()]
b = convert(digits_a, base_a)
if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')
