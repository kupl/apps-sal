n = int(input())
l0 = 2
l1 = 1
sum_ = 1
for i in range(n-1):
    sum_ = l0 + l1
    l0 = l1
    l1 = sum_
print(sum_)
