N = int(input())
r1 = [int(s) for s in input().split()]
r2 = [int(s) for s in input().split()]
sum_max = 0
for e in range(N):
    right = r1[:e + 1]
    left = r2[e:]
    if sum_max < sum(right) + sum(left):
        sum_max = sum(right) + sum(left)
print(sum_max)
