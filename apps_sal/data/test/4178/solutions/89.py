N = int(input())
H = list(map(int, input().split()))
border = H[N - 1]
ans = True
for i in range(N - 2, -1, -1):
    if H[i] <= border:
        border = H[i]
    elif H[i] - 1 <= border:
        border = H[i] - 1
    else:
        ans = False
if ans:
    print('Yes')
else:
    print('No')
