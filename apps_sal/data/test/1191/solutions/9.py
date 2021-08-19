(n, k) = [int(s) for s in input().split()]
p = [int(s) for s in input().split()]
p = [(p[i], i) for i in range(n)]
c = [int(s) for s in input().split()]
c = [[c[i], i] for i in range(n)]
p.sort(key=lambda x: x[0], reverse=True)
c_dic = {}
for x in c:
    c_dic[x[1]] = x[0]
c.sort(key=lambda x: x[0], reverse=True)
ans_set = {}
used = set()
i = 0
cur_ans = 0
cur_k = 0
for j in range(n):
    x = p[j]
    if x[1] not in used:
        used.add(x[1])
    else:
        cur_k -= 1
        cur_ans -= c_dic[x[1]]
    while i < n:
        if cur_k == k:
            break
        if c[i][1] in used:
            i += 1
            continue
        cur_ans += c[i][0]
        cur_k += 1
        used.add(c[i][1])
        i += 1
    ans_set[x[1]] = cur_ans
for i in range(n):
    print(ans_set[i] + c_dic[i], end=' ')
