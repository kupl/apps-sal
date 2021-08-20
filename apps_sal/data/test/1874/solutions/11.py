import math
(l1, l2, l3) = list(map(int, input().split()))
m1 = l1 * l1 - l1 * l1 / 4
h1 = math.sqrt(m1 - m1 / 9)
v1 = l1 * math.sqrt(m1) * h1 / 6
m2 = l2 * l2 - l2 * l2 / 4
h2 = math.sqrt(m2 - l2 * l2 / 4)
v2 = l2 * l2 * h2 / 3
m3 = l3 * l3 - l3 * l3 / 4
x = l3 * math.tan(54 * math.pi / 180) / 2
h3 = math.sqrt(m3 - x * x)
s3 = 5 * l3 * l3 / math.tan(math.pi / 5) / 4
v3 = s3 * h3 / 3
print(v1 + v2 + v3)
