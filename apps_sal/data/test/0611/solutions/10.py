(len, que) = [int(x) for x in input().split(' ')]
total = 0
full = len * (len - 1) // 2
if len % 2 != 0:
    half = len // 2
    half = half * (half + 1)
else:
    half = len // 2
    half = half * half
for i in range(que):
    curr = [int(x) for x in input().split(' ')]
    total += curr[0] * len
    if curr[1] >= 0:
        total += curr[1] * full
    else:
        total += curr[1] * half
print(float(total) / len)
