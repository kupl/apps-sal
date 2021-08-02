from math import ceil
n, k = map(int, input().split())
cou = 0
cou += ceil(n * 2 / k)
cou += ceil(n * 5 / k)
cou += ceil(n * 8 / k)
print(cou)
