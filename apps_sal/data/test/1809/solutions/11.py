
n, m = list(map(int, input().split()))
w = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(m):
    flag = dict()
    for j in range(i - 1, -1, -1):
        if b[j] == b[i]:
            break
        if flag.get(b[j], True):
            ans += w[b[j] - 1]
            flag[b[j]] = False

print(ans)
