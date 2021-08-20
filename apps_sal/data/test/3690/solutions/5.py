(h, m, s, t1, t2) = list(map(int, input().split()))
h = h % 12
t1 = t1 % 12
t2 = t2 % 12
t1 = t1 * 60 * 60
t2 = t2 * 60 * 60
(t1, t2) = (min(t1, t2), max(t1, t2))
hourHand = h * 60 * 60 + m * 60 + s
minHand = (m * 60 + s) * 12
secondHand = s * 60 * 12
count = 0
for val in [hourHand, minHand, secondHand]:
    if val >= t1 and val <= t2:
        count += 1
if count == 0 or count == 3:
    print('YES')
else:
    print('NO')
