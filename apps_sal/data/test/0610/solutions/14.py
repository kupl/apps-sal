def test(begin, r, b):
    bl = b
    rl = r
    if begin == 'b':
        bl -= 1
    else:
        rl -= 1
    last = begin
    pt = 0
    for i in range(r + b - 1):
        if i % 2 == 0:
            if last == 'b':
                if rl > 0:
                    rl -= 1
                    last = 'c'
                else:
                    bl -= 1
                    pt += 1
            else:
                if bl > 0:
                    bl -= 1
                    last = 'b'
                else:
                    rl -= 1
                    pt += 1
        else:
            if last == 'b':
                if bl > 0:
                    bl -= 1
                    pt += 1
                else:
                    rl -= 1
                    last = 'c'
            else:
                if rl > 0:
                    rl -= 1
                    pt += 1
                else:
                    bl -= 1
                    last = 'b'
    return pt


inp = input().split(' ')
r = int(inp[0])
b = int(inp[1])

best = max(test('b', r, b), test('r', r, b))
print(best, r + b - best - 1)
