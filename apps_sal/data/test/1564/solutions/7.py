import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n = int(input())
s = input()
t = input()

x = s.count("a")
y = t.count("a")

if not ((x + y) % 2 == 0 and (2 * n - x - y) % 2 == 0):
    print("-1")
    return


ab = []
ba = []
for i in range(n):
    if s[i] == t[i]:
        continue
    elif s[i] == "a":
        ab.append(i + 1)
    else:
        ba.append(i + 1)

ans = []
while len(ab) >= 2:
    x, y = ab.pop(), ab.pop()
    ans.append((x, y))


while len(ba) >= 2:
    x, y = ba.pop(), ba.pop()
    ans.append((x, y))

if len(ab) + len(ba) == 0:
    print(len(ans))
    for i in ans:
        print(*i)

else:
    x = ab[0]
    y = ba[0]
    ans.append((x, x))
    ans.append((x, y))

    print(len(ans))
    for i in ans:
        print(*i)
