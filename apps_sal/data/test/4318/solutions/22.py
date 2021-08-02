N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
    flag = True
    for j in range(i):
        if H[j] > H[i]:
            flag = False
            break
    if flag: ans += 1

print(ans)
