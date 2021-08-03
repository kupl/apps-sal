n, m = int(input()), list(map(int, input().split()))
a, b = sum(m) // n, (sum(m) + n - 1) // n
print(max(sum(a - x for x in m if x < a), sum(x - b for x in m if x > b)))
