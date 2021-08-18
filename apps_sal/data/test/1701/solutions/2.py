R = lambda type_ = "int": list(map(eval(type_), input().split(' ')))

n, m = R()
d = dict()

for i in range(n):
    a, b = R('str')
    d[b] = a

for i in range(m):
    a, b = R('str')
    print(a + ' ' + b + ' ' + '
