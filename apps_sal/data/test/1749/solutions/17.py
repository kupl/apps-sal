(n, l, r) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0:l - 1] == b[0:l - 1] and a[r:] == b[r:] and (sorted(a[l - 1:r]) == sorted(b[l - 1:r])):
    print('TRUTH')
else:
    print('LIE')
