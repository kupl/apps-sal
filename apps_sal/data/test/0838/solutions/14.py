(n, m) = [int(i) for i in input().split()]
row_one = [0 for i in range(n)]
column_one = [0 for i in range(m)]
for i in range(n):
    tmp = [int(j) for j in input().split()]
    row_one[i] = sum(tmp)
    for j in range(m):
        column_one[j] += tmp[j]
row_zero = [m - i for i in row_one]
column_zero = [n - i for i in column_one]
ans = 0
for i in row_zero:
    ans += 1 << i
for i in column_zero:
    ans += 1 << i
for i in row_one:
    ans += 1 << i
for i in column_one:
    ans += 1 << i
ans = ans - 2 * (m + n) - m * n
print(ans)
