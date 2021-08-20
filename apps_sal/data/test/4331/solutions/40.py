n = input()
count = 0
for i in range(3):
    if n[i] == '7':
        count += 1
if count == 0:
    print('No')
else:
    print('Yes')
