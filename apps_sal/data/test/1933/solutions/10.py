(n, m, k) = map(int, input().split())
sums = [[] for i in range(m)]
for i in range(n):
    str = input().split()
    for j in range(m):
        if i == 0:
            sums[j].append(int(str[j]))
        else:
            sums[j].append(sums[j][i - 1] + int(str[j]))
ans1 = 0
ans2 = 0
for j in range(m):
    cans1 = 0
    cans2 = 0
    for i in range(n):
        if i > 0:
            y = sums[j][i - 1]
        else:
            y = 0
        x = sums[j][min(i + k - 1, n - 1)] - y
        if x > cans1:
            cans1 = x
            cans2 = y
    ans1 += cans1
    ans2 += cans2
print(ans1, ans2)
