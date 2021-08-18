n = int(input())

flag = 'No'

for i in range(0, n // 4 + 2):
    for j in range(0, n // 7 + 2):
        if 4 * i + 7 * j == n:
            flag = 'Yes'
print(flag)
