N = int(input())
H = list(map(int, input().split()))
ans = 0
for i in range(N):
    flg = True
    for j in range(i):
        if H[j] > H[i]:
            flg = False
            break

    if flg:
        ans += 1

print(ans)
