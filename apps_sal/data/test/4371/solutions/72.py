import math
s = list(input())
a = []
for i in range(len(s) - 2):
    p = 100 * int(s[i]) + 10 * int(s[i + 1]) + int(s[i + 2])
    a.append(abs(p - 753))
print(min(a))
