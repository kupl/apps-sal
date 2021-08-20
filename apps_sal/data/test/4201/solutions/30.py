(h, w, k) = list(map(int, input().split()))
li = []
for i in range(h):
    li.append(list(input()))
ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        cnt = 0
        for p in range(h):
            for q in range(w):
                if i >> p & 1:
                    continue
                if j >> q & 1:
                    continue
                if li[p][q] == '#':
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)
