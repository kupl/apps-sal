h, w, k = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        cnt = sum(c[k][l] == '
        if cnt == k:
            ans += 1
print(ans)
