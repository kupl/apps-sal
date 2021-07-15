import math
n, bottles, towels = map(int, input().split())
num = n
cnt = 0
while n != 1:
    cnt += math.floor(math.log2(n))
    n -= math.floor(math.log2(n))
print(cnt * bottles * 2 + cnt, num * towels)
