import bisect

t = int(input())

tmp_ans = [0]*100
for i in range(100):
    tmp_ans[i] = 3**i

ans = []
for i in range(18):
    tmp = ans[0:]
    for j in tmp:
        ans.append(j + tmp_ans[i])
    ans.append(tmp_ans[i])
ans = sorted(ans)

for _ in range(t):
    n = int(input())
    ind = bisect.bisect_left(ans, n)
    print(ans[ind])
