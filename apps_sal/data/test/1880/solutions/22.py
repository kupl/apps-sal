import sys
n = sys.stdin.readline()
m = n[0] + n[2] + n[4] + n[3] + n[1]
m = int(m)
m = m ** 5
m = str(m % 100000)
while len(m) < 5:
    m = '0' + m
print(m)
