import numpy as np

H, W = list(map(int, input().split()))
N = int(input())
a = list(map(int, input().split()))

colors = np.array([[0]*W]*H)

i = 0
j = 0
flag = True
count = 0
for k in range(N):
    for m in range(a[k]):
        colors[i, j] = str(k+1)
        count += 1
        if count % W == 0:
            i += 1
            if flag == True:
                flag = False
            else:
                flag = True
            continue
        if flag == True:
            j += 1
        else:
            j -= 1

for i in range(H):
    s = list(colors[i])
    for j in range(W):
        s[j] = str(s[j])
    p = ' '.join(s)
    print(p)

