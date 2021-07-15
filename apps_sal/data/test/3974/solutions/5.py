a = [1 if x == '+' else -1 for x in input()]
b = list(map(lambda i : sum(a[0:i]), range(len(a) + 1)))
print(max(b) - min(b))
