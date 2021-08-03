s_cnt, b_cnt = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(b_cnt):
    d, g = list(map(int, input().split()))
    b.append((d, g))
b.sort()
idx = [i for i in range(s_cnt)]
idx.sort(key=lambda i: a[i])
ans = [0] * s_cnt
s, j = 0, 0
for i in range(s_cnt):
    while j < b_cnt and b[j][0] <= a[idx[i]]:
        s += b[j][1]
        j += 1
    ans[idx[i]] = s
print(*ans)
