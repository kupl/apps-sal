N = int(input())
H = list(map(int, input().split()))
tmp = -999999
for i in range(N):
    if tmp <= H[i] - 1:
        tmp = H[i] - 1
    elif tmp <= H[i]:
        tmp = H[i]
    else:
        print('No')
        break
else:
    print('Yes')
