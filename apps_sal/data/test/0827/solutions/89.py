n = int(input())
s = input()
x = -(-n // 3)
if s not in '110' * (x + 1):
    print(0)
elif s == '0' or s == '11' or s == '10':
    print(10 ** 10)
elif s == '1':
    print(10 ** 10 * 2)
elif s == '01':
    print(10 ** 10 - 1)
elif s in x * '110':
    print(10 ** 10 - x + 1)
else:
    print(10 ** 10 - x)
