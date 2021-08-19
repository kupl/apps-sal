(l, r, k) = map(int, input().split())
(i, f) = (1, False)
while i <= r:
    if i >= l:
        f = True
        print(i, end=' ')
    i *= k
if not f:
    print('-1')
