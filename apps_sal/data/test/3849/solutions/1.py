import sys


def sum_range(l, r):
    if r < l:
        return 0
    if l == 0:
        return sum[r]
    return sum[r] - sum[l - 1]


n, k = map(int, input().split())

cards = input()

sum = [0] * n
sum[0] = 1 if cards[0] == '1' else 0
for i in range(1, n):
    sum[i] += sum[i - 1]
    if cards[i] == '1':
        sum[i] += 1

min0 = min1 = n
max0 = max1 = -1
for i in range(0, n):
    if cards[i] == '1':
        min1 = min(min1, i)
        max1 = i
    else:
        min0 = min(min0, i)
        max0 = i

toki = False
qual = True
for i in range(0, n - k + 1):
    if sum_range(0, i - 1) + sum_range(i + k, n - 1) + k == n:
        toki = True
    if sum_range(0, i - 1) + sum_range(i + k, n - 1) + 0 == 0:
        toki = True

    prefix = sum_range(0, i - 1) == 0
    suffix = sum_range(i + k, n - 1) == 0
    if i > 0 and i + k < n and (prefix ^ suffix) == 0:
        qual = False
    if i - min0 > k or i - min1 > k or max0 - (i + k - 1) > k or max1 - (i + k - 1) > k:
        qual = False

if toki == True:
    print('tokitsukaze')
elif qual == True:
    print('quailty')
else:
    print('once again')
