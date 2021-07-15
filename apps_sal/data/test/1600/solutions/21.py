__author__ = 'sandeepmellacheruvu'
n = int(input())
arr = list(map(int, input().split()))
sum = 0
blocks = 0
for ai, bi in zip(arr, sorted(arr)):
    sum += ai - bi
    if sum == 0:
        blocks += 1
print(blocks)
