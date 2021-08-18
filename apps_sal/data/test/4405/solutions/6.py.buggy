from collections import Counter
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

c = Counter(A)

LIST = list(c.values())
LIST.sort(reverse=True)

if len(LIST) == 1:
    print(LIST[0])
    return

LL = len(LIST)
y = LIST[0]
ANS = y
if y % 2 == 1:
    y = y - 1

# count2=0
# while y%2==0:
#    y=y//2
#    count2+=1

for x in range(y, 0, -2):
    an = 0
    for j in range(LL):
        if x % (2**j) == 0 and LIST[j] >= x // (2**j):
            an += x // (2**j)
        else:
            break
    if an > ANS:
        ANS = an

print(ANS)
