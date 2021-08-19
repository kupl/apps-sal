import sys
if False:
    inp = open('B.txt', 'r')
else:
    inp = sys.stdin
n = int(inp.readline())
liters = list(map(int, inp.readline().split()))
before = 0
after = 0
low = 10 ** 9 + 10
maxBetween = 0
between = 0
for i in range(n):
    if liters[i] == low:
        after = -1
        maxBetween = max(maxBetween, between)
        between = -1
    if liters[i] < low:
        before = i
        low = liters[i]
        after = -1
        between = -1
        maxBetween = 0
    after += 1
    between += 1
ans = low * n + max(maxBetween, before + after)
print(ans)
