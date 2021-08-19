n = input()
total = 0
for i in n:
    total += int(i)
print('Yes' if total % 9 == 0 else 'No')
