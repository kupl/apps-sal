import datetime
from datetime import datetime as dt
st = input()
tda = dt.strptime(st, '%H:%M')


def isP(s):
    for i in range(len(s)):
        if(s[i] != s[len(s) - i - 1]):
            return False
    return True


for i in range(3600):
    new = tda + datetime.timedelta(minutes=i)
    a = new.strftime('%H:%M')
    if isP(a):
        print(i)
        break
