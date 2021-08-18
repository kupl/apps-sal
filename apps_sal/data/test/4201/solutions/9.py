h, w, k = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
ans = 0

for i in range(2**h):
    for j in range(2**w):
        cnt = 0
        for ih in range(h):
            for iw in range(w):
                if i & (1 << ih) == 0 and j & (1 << iw) == 0 and c[ih][iw] == "
                cnt += 1
        if cnt == k:
            ans += 1
print(ans)
