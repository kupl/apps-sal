m, s = (int(x) for x in input().split())
if s == 0:
    print('0 0' if m == 1 else '-1 -1')
elif s > m * 9:
    print('-1 -1')
else:
    maxs = '9' * (s // 9) + (str(s % 9) if s % 9 else '') + '0' * (m - (s + 8) // 9)
    mins = maxs[::-1]
    if mins[0] == '0':
        nzi = mins.index(next(ch for ch in mins if ch != '0'))
        mins = '1' + mins[1:nzi] + str(int(mins[nzi]) - 1) + mins[nzi + 1:]
    print(mins, maxs)

