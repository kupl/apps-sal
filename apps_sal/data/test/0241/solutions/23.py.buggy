n, m, mn, mx = list(map(int, input().split()))
temps = list(map(int, input().split()))
mnt = min(temps)
mxt = max(temps)
if mnt < mn or mxt > mx:
    print('Incorrect')
    return
if n - m > 1:
    print('Correct')
    return
mnp = mn in temps
mxp = mx in temps
if n - m == 1 and (mnp or mxp):
    print('Correct')
elif mnp and mxp:
    print('Correct')
else:
    print('Incorrect')
