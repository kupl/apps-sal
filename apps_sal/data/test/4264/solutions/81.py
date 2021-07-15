import math

n = int(input())
count = 0

for i in range(n):
    if len(str(i)) % 2 != 0:
        count += 1

if len(str(n)) % 2 == 0:
    count -= 1
    
print(count)
