(h, m) = map(int, input().split(':'))
after = int(input())
afm = h * 60 + m + after
afm %= 24 * 60
print('%.2d:%.2d' % (afm // 60, afm % 60), sep='')
