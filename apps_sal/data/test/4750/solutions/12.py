def fastio():
    import sys
    from io import StringIO
    from atexit import register
    nonlocal input
    sys.stdin = StringIO(sys.stdin.read())
    def input(): return sys.stdin.readline().rstrip('\r\n')
    sys.stdout = StringIO()
    register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


fastio()

MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


n, = I()
while n:
    n -= 1
    a, b, c, d = I()
    if a != c:
        print(a, c)
    elif b != d:
        print(b, d)
    elif a != d:
        print(a, d)
    else:
        print(b, c)
