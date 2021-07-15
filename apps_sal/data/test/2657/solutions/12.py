n = int(input())
aa = list(sorted(map(int, input().split())))
x = max(aa)
y = aa[0]
for i in range(1, n - 1):
    if abs(x / 2 - y) > abs(x / 2 - aa[i]):
        y = aa[i]
print(("{} {}".format(x, y)))

