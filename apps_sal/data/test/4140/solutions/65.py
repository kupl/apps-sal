S = input()
n = len(S)
ans1 = ('01' * 10 ** 6)[:n]
ans2 = ('10' * 10 ** 6)[:n]
count = 0
for (i, j) in zip(S, ans1):
    if i != j:
        count += 1
print(min(count, n - count))
