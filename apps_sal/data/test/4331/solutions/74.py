N = str(input())
count = 0
for i in N:
    if i == '7':
        count = count + 1
if count >= 1:
    print('Yes')
else:
    print('No')
