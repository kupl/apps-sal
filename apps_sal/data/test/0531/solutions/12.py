n = int(input())
meas = [int(x) for x in input().split()]

max_m = int(max(meas))
min_m = int(min(meas))
mid_m = min_m + 1
normalized_meas = [x - min_m for x in meas]

c0 = normalized_meas.count(0)
c2 = normalized_meas.count(2)
c02_pairs = min(c0, c2)
c1 = normalized_meas.count(1)
c1_pairs = c1 // 2

if max_m - min_m < 2:
   print(n)
elif c1_pairs >= c02_pairs:
   print(n - c1 + c1 % 2)
   meas = list(filter(lambda x: x != mid_m, meas))
   meas += [min_m, max_m] * c1_pairs + [mid_m] * (c1 % 2)
else:
   print(n - 2 * c02_pairs)
   meas = list(filter(lambda x: x == mid_m, meas))
   meas += [min_m] * (c0 - c02_pairs) + [max_m] * (c2 - c02_pairs) + [mid_m] * 2 * c02_pairs


print(*meas)
