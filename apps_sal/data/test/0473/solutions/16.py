from datetime import *
a = input().split(":")
b = input().split(":")
x = datetime(1, 1, 3, int(a[0]), int(a[1]))
y = timedelta(hours=int(b[0]), minutes=int(b[1]))
z = str(x - y).split(' ')[1].split(":")
print("%s:%s" % (z[0], z[1]))
