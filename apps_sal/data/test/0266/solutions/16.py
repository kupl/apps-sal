__author__ = 'Rakshak.R.Hegde'
(m, s) = map(int, input().split())
if m == 1 and s == 0:
    print('0 0')
elif s / m > 9 or s == 0:
    print('-1 -1')
else:
    num = [9] * m
    psum = 9 * m
    minDiff = min(8, psum - s)
    num[0] -= minDiff
    psum -= minDiff
    for i in range(1, m):
        minDiff = min(9, psum - s)
        num[i] -= minDiff
        psum -= minDiff
        if psum == s:
            break
    n1 = ''
    for i in num:
        n1 += str(i)
    num = [9] * m
    psum = 9 * m
    for i in range(-1, -m - 1, -1):
        minDiff = min(9, psum - s)
        num[i] -= minDiff
        psum -= minDiff
        if psum == s:
            break
    n2 = ''
    for i in num:
        n2 += str(i)
    print(n1 + ' ' + n2)
