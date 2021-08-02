import sys


n = int(input())
if n == 1:
    print(0)
    return

l = list(map(int, input().split(" ")))
l.sort()
min = l[0]
val = 0
for i in range(1, len(l)):
    if l[i] <= l[i - 1]:
        val += 1 + l[i - 1] - l[i]
        l[i] += 1 + l[i - 1] - l[i]
print(val)
