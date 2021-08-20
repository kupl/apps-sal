(n, m, mi, ma) = map(int, input().split())
a = sorted(list(map(int, input().split())))
if n - m >= 2:
    if a[0] >= mi and a[-1] <= ma:
        print('Correct')
    else:
        print('Incorrect')
elif n - m == 1:
    if a[0] >= mi and a[-1] == ma or (a[0] == mi and a[-1] <= ma):
        print('Correct')
    else:
        print('Incorrect')
elif a[0] == mi and a[-1] == ma:
    print('Correct')
else:
    print('Incorrect')
