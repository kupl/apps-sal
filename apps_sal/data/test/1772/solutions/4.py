import sys
num = int(sys.stdin.readline())
fl = list(map(int, sys.stdin.readline().split()))
odd = 0
even = 0
for f in fl:
    if f % 2:
        odd += 1
    else:
        even += 1
res = min(even, odd)
odd -= even
if odd > 0:
    res += odd // 3
print(res)
