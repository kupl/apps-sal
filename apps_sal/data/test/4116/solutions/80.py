n = int(input())
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag = False
for a in range(1, 10):
    b = n / a
    if b in table:
        flag = True
        break
print('Yes' if flag else 'No')
