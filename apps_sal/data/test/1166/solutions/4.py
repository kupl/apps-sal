n = int(input())
a = [int(i) for i in input().split()]
indx = [0] * n
winners = [''] * n
for (i, ai) in enumerate(a):
    indx[ai - 1] = i
for ai in range(n, 0, -1):
    i = indx[ai - 1]
    can_win = False
    for j in range(i + ai, n, ai):
        if a[j] > ai and 'B' == winners[j]:
            can_win = True
            break
    if not can_win:
        for j in range(i - ai, -1, -ai):
            if a[j] > ai and 'B' == winners[j]:
                can_win = True
                break
    if can_win:
        winners[i] = 'A'
    else:
        winners[i] = 'B'
print(''.join(winners))
