input()

cur = 0
max_value = 0
for c in input():
    x = 1 if c == 'I' else -1
    cur += x
    max_value = max(max_value, cur)

print(max_value)
