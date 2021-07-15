from itertools import groupby

s = input()

cnt = 0

for k, g in groupby(s):
    cnt += 1

print((cnt - 1))

