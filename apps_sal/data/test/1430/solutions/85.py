
N, K = list(map(int, input().split()))
S = input()

l = [0]
curr = '1'
for c in S:
    if c != curr:
        l.append(1)
        curr = c
    else:
        l[-1] += 1
if curr == '0':
    l.append(0)

n_group = len(l) // 2
sum_ = 0
k = min(K, n_group)
for i in range(k):
    sum_ += l[2 * i] + l[2 * i + 1]
sum_ += l[2 * k]
max_ = sum_
for i in range(k, n_group):
    sum_ -= l[2 * i - 2 * K] + l[2 * i + 1 - 2 * K]
    sum_ += l[2 * i + 1] + l[2 * i + 2]
    max_ = max(max_, sum_)
print(max_)
