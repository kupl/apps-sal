(n, m, minn, maxx) = map(int, input().split())
a = sorted(list(map(int, input().split())))
cnt = 0
if minn != a[0]:
    cnt += 1
if maxx != a[-1]:
    cnt += 1
if maxx < a[-1]:
    cnt += 10000000000000000000
if minn > a[0]:
    cnt += 10000000000000000000
if n - m >= cnt:
    print('Correct')
else:
    print('Incorrect')
