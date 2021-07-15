import datetime

def solve(date1,date2):
    d1 = datetime.datetime(int(date1[0]),int(date1[1]),int(date1[2]))
    d2 = datetime.datetime(int(date2[0]),int(date2[1]),int(date2[2]))
    print(abs((d2-d1).days))

date1 = input()
date2 = input()

solve(date1.split(':'),date2.split(':'))

