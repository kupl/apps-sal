(n, k) = (int(input()), int(input()))
x = list(map(int, input().split()))
print(sum([min(i, j) for (i, j) in zip([abs(i * 2) for i in x], [abs((i - k) * 2) for i in x])]))
