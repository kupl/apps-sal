import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

s = rs()
if s == 'RRR':
    a = 3
elif s[:2] == 'RR' or s[1:] == 'RR':
    a = 2
elif s == 'SSS':
    a = 0
else:
    a = 1
print(a)
