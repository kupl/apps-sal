(h, w, k) = map(int, input().split())
c = []
ans = 0
for i in range(h):
    c_i = list(input())
    c.append(c_i)
for i in range(1 << h):
    for j in range(1 << w):
        cnt = 0
        for ii in range(h):
            for jj in range(w):
                if i >> ii & 1:
                    continue
                if j >> jj & 1:
                    continue
                if c[ii][jj] == '#':
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)
