n = int(input())
a = list(map(int, input().split()))
s = sum(a)
l = s // n
if s % n == 0:
    r = l
else:
    r = l + 1
k1 = k2 = 0
for x in a:
    if x < l:
        k1 += l - x
    elif x > r:
        k2 += x - r
print(max(k1, k2))
