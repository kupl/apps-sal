n, k = map(int, input().split())
tds = []
for i in range(n):
    t, d = map(int, input().split())
    tds.append((d, t))
tds.sort(reverse=True)
cnt = k
hand = []
hand_throw = []
hs = {}
subs = []
rs = {}
v_t = {}
res = 0
for i in range(n):
    if cnt > 0:
        if tds[i][1] in hs:
            hs[tds[i][1]] += 1
            hand_throw.append(tds[i][0])
        else:
            hs[tds[i][1]] = 1
            hand.append(tds[i][0])
        cnt -= 1
        res += tds[i][0]
    else:
        if not tds[i][1] in rs and not tds[i][1] in hs:
            rs[tds[i][1]] = 1
            subs.append(tds[i][0])
    if not tds[i][1] in v_t:
        v_t[tds[i][1]] = 1
subs.sort()
v_hs = len(hs)
v_t = len(v_t)
res += pow(v_hs, 2)
final_res = res
while v_hs + 1 <= k and v_hs + 1 <= v_t:
    res += subs.pop() - hand_throw.pop() - pow(v_hs, 2) + pow(v_hs + 1, 2)
    final_res = max(final_res, res)
    v_hs += 1
print(final_res)
