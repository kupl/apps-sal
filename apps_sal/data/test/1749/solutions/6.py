(n, l, r) = map(int, input().split())
a = input().split()
b = input().split()
if a[:l - 1] == b[:l - 1] and a[r:] == b[r:]:
    print('TRUTH')
else:
    print('LIE')
