x, y = list(map(int, input().split()))
assert y < x

it = 0

a, b, c = y, y, y
while True:
    assert a >= c >= b
    assert a + b > c
    assert a + c > b
    assert b + c > a

    b = a + c - 1

    assert a + b > c
    assert a + c > b
    assert b + c > a

    it += 1
    if b >= x:
        b = x
        break
    a, b, c = b, c, a

b = x
it += 1
assert a + b > c
assert a + c > b
assert b + c > a

c = x
it += 1
assert a + b > c
assert a + c > b
assert b + c > a

print(it)
