n = int(input())
rs = [int(num) - 100 for num in input().split()]
sums = [0]
sum_ = 0
for i in range(n):
    sum_ += rs[i]
    sums.append(sum_)
max_len = 0
for i in range(n + 1):
    for j in range(n + 1):
        len_ = j - i
        if len_ <= max_len:
            continue
        sum_ = sums[j] - sums[i]
        if sum_ > 0:
            max_len = len_
print(max_len)
