n = int(input())
cnt = 0
for i in range(26):
    for j in range(15):
        if i*4 +j*7 == n:
            cnt += 1
        else:
            continue
if cnt != 0:
    print('Yes')
else:
    print('No')
