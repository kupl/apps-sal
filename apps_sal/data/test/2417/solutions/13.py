""" ----------------------------------------------------------------------------------------------------  """
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
' ----------------------------------------------------------------------------------------------------  '
' ----------------------------------------------------------------------------------------------------  '


def li():
    return [int(i) for i in input().rstrip('\n').split(' ')]


def val():
    return int(input().rstrip('\n'))


def st():
    return input().rstrip('\n')


def sttoli():
    return [int(i) for i in input().rstrip('\n')]


' ----------------------------------------------------------------------------------------------------  '
' ----------------------------------------------------------------------------------------------------  '
n = val()
l1 = li()
l2 = li()
d = {}
t = 0
for i in l1:
    d[i] = t
    t += 1
s = set()
t = 0
tot = 0
for i in l2:
    if d[i] != t:
        tot += 1
        s.add(d[i])
    else:
        t += 1
        while t in s:
            t += 1
print(tot)
' ----------------------------------------------------------------------------------------------------  '
