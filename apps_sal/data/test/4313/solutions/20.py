n = int(input())

v = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]

sum_ = 0
for i in range(n):
    if v[i] - c[i] > 0:
        sum_ += v[i] - c[i]
print(sum_)
