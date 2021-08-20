n = int(input())
hl = list(map(int, input().split()))
hl[0] -= 1
flag = True
for i in range(1, n):
    if hl[i] > hl[i - 1]:
        hl[i] -= 1
    elif hl[i] == hl[i - 1]:
        continue
    else:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
