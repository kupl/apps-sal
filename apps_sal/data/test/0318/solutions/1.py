import datetime
import time

t = input()
M = input()
h, m = list(map(int, t.split(':')))

H, M = divmod(int(M), 60)

a = datetime.datetime(100, 1, 1, h, m, 00)
b = a + datetime.timedelta(0, 0, 0, 0, M, H, 0)
print(b.strftime('%H:%M'))
