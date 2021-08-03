import sys
n, k = list(map(int, input().split()))
v = k
k -= 1
sum = 0
for i in range(1, n + 1):
    if ((k - sum) % 2 == 0):
        print(i)
        break
    sum += v // (1 << i)
