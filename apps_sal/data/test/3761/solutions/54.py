s = input().split('T')
(x, y) = map(int, input().split())
xmove = []
ymove = []
for i in range(len(s)):
    if i % 2 == 1:
        ymove.append(s[i].count('F'))
    else:
        xmove.append(s[i].count('F'))


def solve(l, cor):
    dp = {0}
    for c in l:
        dp = {c + i for i in dp} | {i - c for i in dp}
    return cor in dp


if solve(xmove[1:], x - xmove[0]) and solve(ymove, y):
    print('Yes')
else:
    print('No')
