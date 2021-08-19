(n, m, mi, ma) = tuple(map(int, str.split(input())))
ts = tuple(map(int, str.split(input())))
if max(ts) > ma or min(ts) < mi:
    ans = 'Incorrect'
else:
    count = 2
    if mi in ts:
        count -= 1
    if ma in ts:
        count -= 1
    if n - m >= count:
        ans = 'Correct'
    else:
        ans = 'Incorrect'
print(ans)
