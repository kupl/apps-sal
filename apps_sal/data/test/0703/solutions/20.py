str_ = input()
items = str_.strip().split()
k = int(items[0])
a = int(items[1])
b = int(items[2])
v = int(items[3])
sum_ = 0
ans = 0
while sum_ < a:
    if b != 0:
        sum_ += min(k, b + 1) * v
        b = max(0, b - k + 1)
    else:
        sum_ += v
    ans += 1
print(str(ans) + '\n')
