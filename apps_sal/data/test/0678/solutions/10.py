tux = int(input())
foo = 0
bar = 0
baz = 0
quz = 1
for i in range(0, tux):

    pur = int(input())

    foo += pur
    bar += 1
    if foo * quz > baz * bar:
        baz = foo
        quz = bar
print('%.6f' % (baz / quz))
