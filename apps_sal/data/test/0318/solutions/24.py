h, m = map(int, input().split(':'))
v = 60 * h + m + int(input())
print('{:02}:{:02}'.format(v // 60 % 24, v % 60))
