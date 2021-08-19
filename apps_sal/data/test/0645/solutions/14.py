s = input()
result = 0
for c in s:
    if c in ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']:
        result += 1
print(result)
