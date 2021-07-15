
yes_count = 0
for count in range(int(input())):
    a,b = input().split()
    if a == b:
        yes_count += 1
    else:
        if yes_count < 3:
            yes_count = 0
if yes_count >= 3:
    print('Yes')
else:
    print('No')

