from collections import Counter
import math
import sys
x = int(input())

if x == 1:
    print(1, 0)
    return

TWO = [2**i for i in range(30)]

xr = math.ceil(math.sqrt(x))

LIST = []
for i in range(2, xr + 2):
    if x % i == 0:
        while x % i == 0:
            LIST.append(i)
            x = x // i
    else:
        i += 1
if x != 1:
    LIST.append(x)

counter = Counter(LIST)

ANS = 1
for l in list(counter.keys()):
    ANS *= l

count = max(counter.values())

for i in range(30):
    if count <= TWO[i]:
        break

if max(counter.values()) == min(counter.values()) and TWO[i] == max(counter.values()):
    ANS2 = i
else:
    ANS2 = i + 1

print(ANS, ANS2)
