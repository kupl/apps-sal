def win(x, y):
    if x + y in ['PR', 'RP', 'PP']:
        return 'P'
    if x + y in ['SR', 'RS', 'RR']:
        return 'R'
    if x + y in ['SP', 'PS', 'SS']:
        return 'S'

n, k = list(map(int, input().split()))
s = list(input()[::-1]) * 2

for _ in range(k):
    tmp = []
    while s:
        i, j = s.pop(), s.pop()
        tmp.append(win(i, j))
    s = tmp[::-1] * 2
print((s.pop()))

