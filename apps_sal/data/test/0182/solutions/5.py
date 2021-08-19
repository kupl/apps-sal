import math
Own = list(map(int, input().split()))
Req = list(map(int, input().split()))
Delta = 0
for i in range(3):
    Delta += math.floor((Own[i] - Req[i]) / 2) if Own[i] > Req[i] else Own[i] - Req[i]
print('Yes' if Delta >= 0 else 'No')
