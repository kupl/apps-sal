(n, m, mmin, mmax) = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
if s[0] < mmin or s[m - 1] > mmax:
    print('Incorrect')
elif s[0] == mmin and s[m - 1] == mmax:
    print('Correct')
elif s[0] != mmin and s[m - 1] != mmax:
    if n - m < 2:
        print('Incorrect')
    else:
        print('Correct')
elif s[0] != mmin or s[m - 1] != mmax:
    if n - m < 1:
        print('Incorrect')
    else:
        print('Correct')
