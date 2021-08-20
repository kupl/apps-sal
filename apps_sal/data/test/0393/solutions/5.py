a = input()
b = input() + '0'
zeros = 1
ans = True
for c in b:
    if c == '1':
        if zeros == 0:
            ans = False
        zeros = 0
    else:
        zeros = zeros + 1
        if zeros > 2:
            ans = False
if ans:
    print('Yes')
else:
    print('No')
