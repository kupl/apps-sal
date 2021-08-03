import sys
import math
import itertools as it
import operator as op
import fractions as fr


a, ta = map(int, sys.stdin.readline().split())
b, tb = map(int, sys.stdin.readline().split())
sh, sm = map(int, sys.stdin.readline().strip().split(':'))

sme = sh * 60 + sm


start = sme - tb
end = sme + ta

last_bus_B_min = int(math.ceil((19 * 60) / b)) * b + 300
sch_B = list(range(300, last_bus_B_min, b))

t = filter(lambda t: (t > start) and (t < end), sch_B)
print(len(list(t)))
