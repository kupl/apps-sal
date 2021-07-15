#!/usr/bin/env python3

n = int(input())
arr = list(map(int, input().split()))
assert len(arr) == n

total = sum(arr)
avg1 = total // n
avg2 = avg1 + (0 if total % n == 0 else 1)

seconds = 0
offset = 0
for n in arr:
    if n < avg1:
        seconds += (avg1 - n)
        offset += (avg1 - n)
    elif n > avg2:
        seconds += (n - avg2)
        offset += (avg2 - n)

seconds = (seconds + abs(offset)) // 2
print(seconds)

