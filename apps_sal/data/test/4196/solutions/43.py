from math import gcd
from collections import deque
n = int(input())
a = list(map(int, input().split()))
a_left = deque()

a_left.append(a[0])


a_right = deque()

a_right.append(a[-1])

for i in range(n - 1):
    a_left.append(gcd(a_left[-1], a[i + 1]))
    a_right.appendleft(gcd(a_right[0], a[n - i - 2]))


a_right = list(a_right)
a_left = list(a_left)

count = max(a_left[-2], a_right[1])

for j in range(n - 2):
    count = max(gcd(a_left[j], a_right[j + 2]), count)
print(count)
