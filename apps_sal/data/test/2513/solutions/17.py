def get_next(sw_prev2, sw_prev1, ox_prev1):
    rev_ox = {'o': 'x', 'x': 'o'}
    rev_sw = {'S': 'W', 'W': 'S'}
    sw = sw_prev2
    if sw_prev1 == 'W':
        ox_prev1 = rev_ox[ox_prev1]
    if ox_prev1 == 'x':
        sw = rev_sw[sw]
    return sw


n = int(input())
ox = input()
for (sw0, sw1) in [('S', 'S'), ('S', 'W'), ('W', 'S'), ('W', 'W')]:
    ans = ''
    ans = sw0 + sw1
    for (i, oxi) in enumerate(ox[1:] + ox[0], 1):
        ans += get_next(ans[i - 1], ans[i], oxi)
    if ans[0] == ans[-2] and ans[1] == ans[-1]:
        ans = ans[:-2]
        break
else:
    ans = -1
print(ans)
