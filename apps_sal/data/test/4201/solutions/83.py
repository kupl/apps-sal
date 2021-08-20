(h, w, k) = list(map(int, input().split()))
s = [list(map(str, list(input()))) for i in range(h)]
ans = 0
for ii in range(1 << h):
    for jj in range(1 << w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if ii >> i & 1:
                    continue
                if jj >> j & 1:
                    continue
                if s[i][j] == '#':
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)
