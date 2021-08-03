import sys

n = int(sys.stdin.readline())
s = ""
if (n % 2 == 1):
    n -= 3
    s = "7"

for i in range(0, n, 2):
    s += "1"
print(s)
