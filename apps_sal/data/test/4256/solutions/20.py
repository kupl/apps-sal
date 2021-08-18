def input2():
    return map(int, input().split())


a, b, c = input2()
if b // a >= c:
    print(c)
else:
    print(b // a)
