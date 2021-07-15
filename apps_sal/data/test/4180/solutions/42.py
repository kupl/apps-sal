from math import ceil
buy = int(input())
pay = ceil(buy / 1000) * 1000
oturi = pay - buy
print(oturi)
