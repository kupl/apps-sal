import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
n = int(input())
a = list(map(int, input().split()))
(r1, c1, r2, c2) = list(map(int, input().split()))
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1
sign = 1 if r2 - r1 >= 0 else -1
for i in range(abs(r2 - r1) + 1):
    c1 = min(c1, a[r1 + sign * i])
res1 = 0
for i in range(min(r1, r2)):
    tmp = (min(r1, r2) - i) * 2
    if c1 > max(c2, a[i]) and a[i] <= min(a[i:min(r1, r2)]):
        tmp -= c1 - c2 - abs(a[i] - c2)
    res1 = min(res1, tmp)
res2 = 0
for i in range(max(r1, r2) + 1, n):
    tmp = (i - max(r1, r2)) * 2
    if c1 > max(c2, a[i]) and a[i] <= min(a[max(r1, r2):i]):
        tmp -= c1 - c2 - abs(a[i] - c2)
    res2 = min(res2, tmp)
print(min(res1, res2) + abs(r2 - r1) + abs(c1 - c2))
