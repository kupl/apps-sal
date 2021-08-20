N = int(input())
flag = 0
if N % 4 == 0 or N % 7 == 0:
    flag = 1
else:
    out = N // 7
    for i in range(out):
        if (N - 7 * (i + 1)) % 4 == 0:
            flag = 1
            break
if flag == 1:
    print('Yes')
else:
    print('No')
