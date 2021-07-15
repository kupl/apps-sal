
res = 0
i = 0
for word in input().split('heavy'):
    res += i * word.count('metal')
    i += 1

print(res)

