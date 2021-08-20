(n, m, k) = map(int, input().split())
x = [*map(int, input().split())]
diff = []
for i in range(n - 1):
    diff.append([x[i + 1] - x[i] - 1, i])
diff.sort(reverse=True)
ori = x[-1] - x[0] + 1
for i in range(k - 1):
    ori -= diff[i][0]
print(ori)
