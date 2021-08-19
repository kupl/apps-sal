(a, b, c, d) = map(int, input().split())
takahashi_turn = 0
aoki_turn = 0
while c - b > 0:
    takahashi_turn += 1
    c -= b
while a - d > 0:
    aoki_turn += 1
    a -= d
if takahashi_turn <= aoki_turn:
    print('Yes')
else:
    print('No')
