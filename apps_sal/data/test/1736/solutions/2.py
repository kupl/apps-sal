import sys
f = sys.stdin
# f = open("input.txt", "r")
n, t = map(int, f.readline().split())
a = [int(i) for i in f.readline().strip().split()]
s = 0
res = 0
left, right = 0, 0
while left < n:
    while right < n and s+a[right] <= t:
        s += a[right]
        right += 1
    res = max(res, right-left)
    s -= a[left]
    left += 1
print(res)
