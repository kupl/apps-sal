import math

input()
seq = [0] + [int(i) for i in input().split()]
cum = [0] + [abs(seq[i - 1] - seq[i]) if i > 1 else 0 for i in range(1, len(seq))]

mx = -math.inf

eve = [0] * len(cum)
odd = [0] * len(cum)

for i in range(2, len(cum)):
    eve[i] = max(cum[i], odd[i - 1] + cum[i])
    odd[i] = max(-cum[i], eve[i - 1] - cum[i])
    mx = max(mx, odd[i], eve[i])

print(mx)
