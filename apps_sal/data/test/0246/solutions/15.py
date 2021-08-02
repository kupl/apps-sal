n, s = [int(i) for i in input().split()]
print(max(n - ([i for i in range(s, s + 9 * 18 + 1) if i - sum([int(j) for j in str(i)]) >= s] + [int('1' * 18)])[0] + 1, 0))
