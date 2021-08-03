
import math
N = int(input())

result = []

for i in range(1, 9 + 1):
    if N % i == 0 and N // i < 10:
        result.append(i)

if len(result) == 0:
    print('No')

else:
    print('Yes')
