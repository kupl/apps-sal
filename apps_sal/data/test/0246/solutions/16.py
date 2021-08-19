(n, s) = [int(i) for i in input().split()]
print(max(n - [i for i in range(s, s + 180) if i - sum([int(j) for j in str(i)]) >= s][0] + 1, 0))
