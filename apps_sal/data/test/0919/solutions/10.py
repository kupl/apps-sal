from collections import defaultdict
import string

n, k = [int(i) for i in input().split()]
x = input()
d = {}
for i in string.ascii_lowercase:
    d[i] = i in x
i = 0
count = 0
while i < 26 and k > 0:
    if d[string.ascii_lowercase[i]]:
        count += i + 1
        i += 2
        k -= 1
    else:
        i += 1

if k > 0:
    print(-1)
else:
    print(count)
