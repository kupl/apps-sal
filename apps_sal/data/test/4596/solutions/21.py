N = int(input())
A = list(map(int, input().split()))
ans = 0
while 1:
    flg = 0
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            flg = 1
            break
    if flg == 1:
        break
    ans += 1
print(ans)
