N = int(input())
H = list(map(int, input().split()))
flag = True
for i in range(1, len(H))[::-1]:
    if H[i] >= H[i - 1]:
        pass
    elif H[i] + 1 == H[i - 1]:
        H[i - 1] = H[i - 1] - 1
    else:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
