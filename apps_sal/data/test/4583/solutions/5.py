a, b, c, d = map(int, input())
if a + b - c + d == 7:
    print('%d+%d-%d+%d=7' % (a, b, c, d))
    return
elif a + b - c - d == 7:
    print('%d+%d-%d-%d=7' % (a, b, c, d))
    return
elif a - b - c + d == 7:
    print('%d-%d-%d+%d=7' % (a, b, c, d))
    return
elif a - b - c - d == 7:
    print('%d-%d-%d-%d=7' % (a, b, c, d))
    return
elif a + b + c + d == 7:
    print('%d+%d+%d+%d=7' % (a, b, c, d))
    return
elif a + b + c - d == 7:
    print('%d+%d+%d-%d=7' % (a, b, c, d))
    return
elif a - b + c + d == 7:
    print('%d-%d+%d+%d=7' % (a, b, c, d))
    return
elif a - b + c - d == 7:
    print('%d-%d+%d-%d=7' % (a, b, c, d))
    return
