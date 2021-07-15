n = int(input())
alst = list(map(int, input().split()))
max_ = max(alst)
min_ = min(alst)
max_ind = alst.index(max_)
min_ind = alst.index(min_)
print(2 * n - 1)
if abs(max_) > abs(min_):
    for i in range(n):
        print(max_ind + 1, i + 1)
    for i in range(n - 1):
        print(i + 1, i + 2)
else:
    for i in range(n):
        print(min_ind + 1, i + 1)
    for i in range(n, 1, -1):
        print(i, i - 1)
