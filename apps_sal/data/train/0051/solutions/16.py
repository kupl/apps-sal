from sys import *

t = int(stdin.readline())
mm = 0
for i in range(t):
    n, k, d1, d2 = (int(z) for z in stdin.readline().split())
    mm = 2 * max(d1, d2) - min(d1, d2)
    if (k - 2 * d1 - d2 >= 0 and (k - 2 * d1 - d2) % 3 == 0 and n - 2 * d2 - d1 - k >= 0 and (n - 2 * d2 - d1 - k) % 3 == 0) or (k - 2 * d2 - d1 >= 0 and (k - 2 * d2 - d1) % 3 == 0 and n - 2 * d1 - d2 - k >= 0 and (n - 2 * d1 - d2 - k) % 3 == 0) or (k - d1 - d2 >= 0 and (k - d1 - d2) % 3 == 0 and n - mm - k >= 0 and (n - mm - k) % 3 == 0) or (k - mm >= 0 and (k - mm) % 3 == 0 and n - d1 - d2 - k >= 0 and (n - d1 - d2 - k) % 3 == 0):
        print("yes")
    else:
        print("no")
