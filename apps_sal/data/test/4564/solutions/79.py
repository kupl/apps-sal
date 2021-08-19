str = input()
count = 0
table = list(str)
for i in range(len(str) - 1):
    for j in range(i + 1, len(str)):
        if table[i] == table[j]:
            count += 1
if count == 0:
    print('yes')
else:
    print('no')
