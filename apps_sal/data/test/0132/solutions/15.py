n = int(input())
ar = [int(i) for i in input().split(' ')]
sum = 0
s_a = 1000
for i in range(n):
    k = 0
    sum = 0
    while sum < 180:
        sum += ar[i - k]
        k += 1
    if s_a > sum - (360 - sum):
        s_a = sum - (360 - sum)
print(s_a)
