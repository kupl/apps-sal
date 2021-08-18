import re
input()
a = list(map(int, input().split()))
b = input()
l, r = -10**9, 10**9

for m in re.finditer("11110", b):
    i = m.start(0)
    r = min([r + 1] + a[i:i + 5]) - 1

for m in re.finditer("00001", b):
    i = m.start(0)
    l = max([l - 1] + a[i:i + 5]) + 1

print(l, r)
