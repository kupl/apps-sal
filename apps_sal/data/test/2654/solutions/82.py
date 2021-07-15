import statistics
from collections import Counter
N = int(input())
A = [list(map(int, input().split(" "))) for i in range(N)]
xMIN = []
xMAX = []



for i in range(N):
    xMIN.append(A[i][0])

for j in range(N):
    xMAX.append(A[j][1])


if N % 2 != 0:
    medianMIN = statistics.median(xMIN)
    medianMAX = statistics.median(xMAX)
    print((int(medianMAX-medianMIN+1)))
else:
    medianMIN_LOW = statistics.median_low(xMIN)
    medianMIN_HIGH = statistics.median_high(xMIN)
    medianMAX_LOW = statistics.median_low(xMAX)
    medianMAX_HIGH = statistics.median_high(xMAX)
    print(((medianMAX_LOW+medianMAX_HIGH)-(medianMIN_LOW+medianMIN_HIGH)+1))

