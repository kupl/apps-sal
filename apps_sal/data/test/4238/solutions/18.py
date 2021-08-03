import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]


N = [int(i) for i in rs()]
print('Yes' if sum(N) % 9 == 0 else 'No')
