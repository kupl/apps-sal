import datetime
a, b, c = map(int, input().split(':'))
d1 = datetime.date(a, b, c)
a, b, c = map(int, input().split(':'))
d2 = datetime.date(a, b, c)
d3 = abs(d2 - d1)
print(d3.days)
