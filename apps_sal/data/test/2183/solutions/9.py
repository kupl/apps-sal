a, b = list(map(int, input().split()))
q = list({1, 2, 3} - {a, b})[0]
print(q)
