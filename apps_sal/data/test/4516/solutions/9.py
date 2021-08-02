def pos(x, i):
    if x > i:
        return x
    elif x < i:
        return x + 1
    else:
        return 1


n, m = map(int, input().split())
x = list(map(int, input().split()))
delta_ = [0] * (n + 2)
func = sum(abs(x[i + 1] - x[i]) for i in range(m - 1))
for i in range(m):
    if x[i] < n:
        if i > 0:
            prev_l = abs(pos(x[i], x[i]) - pos(x[i - 1], x[i]))
            cur_l = abs(pos(x[i], x[i] + 1) - pos(x[i - 1], x[i] + 1))
            delta_[x[i] + 1] += cur_l - prev_l
        if i < m - 1:
            prev_r = abs(pos(x[i], x[i]) - pos(x[i + 1], x[i]))
            cur_r = abs(pos(x[i], x[i] + 1) - pos(x[i + 1], x[i] + 1))
            delta_[x[i] + 1] += cur_r - prev_r
    if x[i] > 1:
        if i > 0:
            prev_l = abs(pos(x[i], x[i] - 1) - pos(x[i - 1], x[i] - 1))
            cur_l = abs(pos(x[i], x[i]) - pos(x[i - 1], x[i]))
            delta_[x[i]] += cur_l - prev_l
        if i < m - 1:
            prev_r = abs(pos(x[i], x[i] - 1) - pos(x[i + 1], x[i] - 1))
            cur_r = abs(pos(x[i], x[i]) - pos(x[i + 1], x[i]))
            delta_[x[i]] += cur_r - prev_r

for i in range(1, n + 1):
    print(func, end=" ")
    func += delta_[i + 1]
