n, a = int(input()), list(map(int, input().split()))
sums, s = [[0, 0]] + [0] * n, sum(a)
for i in range(n):
    sums[i + 1] = [sums[i][0] + a[i], sums[i][1] + int(i != n - 1 and (sums[i][0] + a[i]) * 3 == s * 2)]
print(0 if s % 3 else sum(sums[-1][1] - sums[i][1] for i in range(1, n) if sums[i][0] * 3 == s))
