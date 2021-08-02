input(); a, b1, b2, b4 = list(map(int, input().split())), 0, 0, 0
for i in a:
    if i % 2 != 0: b1 += 1
    elif i % 4 == 0: b4 += 1
    else: b2 += 1
print('Yes'if b1 <= b4 else'No'if b2 else'Yes'if b1 <= b4 + 1 else'No')
