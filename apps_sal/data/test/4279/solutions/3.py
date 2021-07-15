import bisect


tmp_ans = 0
len_prev = 0
li = [0]
for i in range(1,1000000):
    tmp = len(str(i))
    len_prev += tmp
    tmp_ans += len_prev
    li.append(tmp_ans)

ans = []
for num in range(1,1000000):
    for i in str(num):
        ans.append(i)

q = int(input())
for i in range(q):
    k = int(input())
    pos = bisect.bisect_left(li, k)
    k -= li[pos - 1]
    print(ans[k - 1])


