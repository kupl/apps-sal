import math
n = int(input())
cel = math.floor(n / 7)
ost = n % 7
if ost <= 2:
    max_weekend = cel * 2 + ost
else:
    max_weekend = cel * 2 + 2
if ost < 6:
    min_weekend = cel * 2
else:
    min_weekend = cel * 2 + 7 - ost
print(min_weekend, max_weekend)

