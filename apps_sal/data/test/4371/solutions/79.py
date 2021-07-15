table = list(map(int, input()))
diff_nagomi = 1000
ans = 0
for i in range(len(table)-2):
    diff = abs(table[i] * 100 + table[i + 1] * 10 + table[i + 2] - 753)
    if diff_nagomi > diff:
        ans = diff
        diff_nagomi = diff
print(ans)

