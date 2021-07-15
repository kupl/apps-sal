w = list(input())

w.sort()

cnt = 1

for i in range(len(w)-1):
    if w[i] != w[i+1]:
        if cnt % 2 == 1:
            print('No')
            return
        else:
            cnt = 1
    else:
        cnt += 1

if cnt % 2 == 1:
    print('No')
else:
    print('Yes')
