from itertools import groupby
s = input()
count = 0
for (k, g) in groupby(s):
    count += 1
print(count - 1)
