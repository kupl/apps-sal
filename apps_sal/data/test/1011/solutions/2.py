import bisect
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)


mx = -5555555555555
aa = -5555555555555555
bb = -5555555555555555

cands = list(a + b)
cands.append(0)
cands.append(3000000009)

for v in cands:
    q1 = len(a) - bisect.bisect_left(a, v)
    q2 = len(b) - bisect.bisect_left(b, v)
    c1 = q1 * 3 + 2 * (len(a) - q1)
    c2 = q2 * 3 + 2 * (len(b) - q2)
    if (c1 - c2 > mx) or (c1 - c2 == mx and c1 > aa):
        mx = c1 - c2
        aa = c1
        bb = c2

print(str(aa) + ':' + str(bb))
