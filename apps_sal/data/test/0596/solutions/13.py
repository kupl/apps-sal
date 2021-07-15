from datetime import *
R = lambda: datetime(*map(int, input().split(':')))
date1 = R()
date2 = R()
print(abs(date2 - date1).days)
