A, B = map(int, input().split())
plus = A+B
minus = A-B
mult = A*B

if plus >= minus and plus >= mult:
    print(plus)
elif minus >= plus and minus >= mult:
    print(minus)
elif mult >= plus and mult >= minus:
    print(mult)
