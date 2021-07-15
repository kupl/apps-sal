n = int(input())
f = n // 4
s = n // 7

flag = False
for i in range(f + 1):
    for j in range(s + 1):
        total = i * 4 + j * 7
        if total == n:
            flag = True
            break

if flag:
    print('Yes')
else:
    print('No')
