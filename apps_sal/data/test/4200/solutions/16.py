(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
total = sum(a)
print('Yes' if sum([4 * m * A >= total for A in a]) >= m else 'No')
