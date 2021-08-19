def vals():
    return map(int, input().split())


(n, l, r) = vals()
a1 = list(vals())
a2 = list(vals())
if a1[:l - 1] == a2[:l - 1] and a1[r:] == a2[r:]:
    print('TRUTH')
else:
    print('LIE')
