import sys
def input(): return sys.stdin.readline().rstrip()
import math

X = int(input())

ans = False
money = 100
year = 0
while money < X:
    money += money // 100
    year += 1

print(year)

