a = input()
N = int(a)
H = list(map(int,input().split()))

flag = 1
H[0] = H[0] - 1

for i in range(1,N):
    if H[i-1] < H[i]:
        H[i] = H[i] - 1
    elif H[i-1] > H[i]:
        flag = 0
        break
if flag == 1:
    print('Yes')
else:
    print('No')
