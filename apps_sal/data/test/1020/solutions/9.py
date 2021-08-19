(w, h, k) = list(map(int, input().split()))
sum_ = 0
for i in range(k):
    sum_ += (w - 4 * i + h - 4 * i) * 2 - 4
print(sum_)
