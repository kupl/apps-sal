import math
import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))


minuses = 0
diff = []
for i in range(1, len(li)):
    diff.append(li[i] - li[i - 1])
    if li[i] < li[i - 1]:
        minuses += (li[i - 1] - li[i])

ll = li[-1]
print(math.ceil((minuses + ll) / 2))

for i in range(int(input())):
    l, r, x = list(map(int, input().split()))
    if l > 1:
        old = diff[l - 2]
        diff[l - 2] += x
        minuses += max(-(old + x), 0) - max(-old, 0)

    if r < n:
        old = diff[r - 1]
        diff[r - 1] -= x
        minuses += max(-(old - x), 0) - max(-old, 0)

    if r == n:
        ll += x

    print(math.ceil((minuses + ll) / 2))
