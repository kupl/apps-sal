import sys
MOD = 10 ** 9 + 7
INF = float('inf')
N = int(input())
A = list(map(int, input().split()))
Aafter = [A[i] - (i + 1) for i in range(N)]
minus = []
zero_count = 0
plus = []
for i in range(N):
    if Aafter[i] < 0:
        minus.append(-Aafter[i])
    elif Aafter[i] == 0:
        zero_count += 1
    else:
        plus.append(Aafter[i])
minus.sort()
plus.sort()
minus_count = len(minus)
plus_count = len(plus)
bias = 0
if minus_count + zero_count < plus_count:
    dif = (plus_count - (minus_count + zero_count)) // 2
    bias = plus[dif]
elif plus_count + zero_count < minus_count:
    dif = (minus_count - (plus_count + zero_count)) // 2
    bias = -minus[dif]
res = 0
for i in range(N):
    res += abs(Aafter[i] - bias)
print('{}'.format(res))
