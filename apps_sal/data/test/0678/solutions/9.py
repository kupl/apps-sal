tux = int(input())
foo = 0
bar = 0
baz = 0
quz = 1
while tux > 0:
    tux -= 1
    pur = int(input())
    foo += pur
    bar += 1
    if max(foo * quz, bar * baz) == foo * quz:
        baz = foo
        quz = bar
print(baz / quz)
