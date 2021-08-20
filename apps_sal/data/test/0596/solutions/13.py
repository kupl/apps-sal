from datetime import *


def R():
    return datetime(*map(int, input().split(':')))


date1 = R()
date2 = R()
print(abs(date2 - date1).days)
