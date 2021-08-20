(a, b) = input().split()
s = int(a + b)
result = 'No'
for i in range(1, round(s)):
    if s / i == i:
        result = 'Yes'
print(result)
