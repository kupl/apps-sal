import math
n = int(input())
a = list(map(int, input().split()))
ra = list(reversed(a))
left = []
right = []
right.append(ra[0])
left.append(a[0])
if n > 2:
    k = math.gcd(a[0], a[1])
    left.append(k)
    for i in range(2, n - 1):
        k = math.gcd(k, a[i])
        left.append(k)
    k = math.gcd(ra[0], ra[1])
    right.append(k)
    for i in range(2, n - 1):
        k = math.gcd(k, ra[i])
        right.append(k)
    ans = [right[-1]]
    for i in range(1, n - 1):
        ans.append(math.gcd(left[i - 1], right[len(right) - i - 1]))
    ans.append(left[-1])
    print(max(ans))
else:
    print(max(a[1], a[0]))
