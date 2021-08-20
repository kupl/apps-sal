(h, w) = map(int, input().split())
a_l = [['#'] + list(map(str, input().split())) + ['#'] for i in range(h)]
print(''.join(['#'] * (w + 2)))
for a in a_l:
    print(''.join(a))
print(''.join(['#'] * (w + 2)))
