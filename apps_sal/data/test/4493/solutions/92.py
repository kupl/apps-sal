c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

sw = 1
b1 = min(c1)
a = [c1[0] - b1, c1[1] - b1, c1[2] - b1]

if not(c2[0] - a[0] == c2[1] - a[1] == c2[2] - a[2]):
    sw = 0
if not(c3[0] - a[0] == c3[1] - a[1] == c3[2] - a[2]):
    sw = 0

print((["No", "Yes"][sw]))
