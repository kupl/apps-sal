def iig(vn, en):
    res = [[] for _ in range(vn)]
    for _ in range(en):
        ai, bi = map(lambda x: int(x) - 1, input().split())
        res[ai].append(bi)
    return res

n, m = map(int, input().split())
v = iig(n, m)

nxtsum = [0] * n
e = [0] * n
for i, adjl in reversed(list(enumerate(v))):
	count = len(adjl)
	if count == 0:
		continue
	nxtsum[i] = sum(e[nxt] for nxt in adjl)
	e[i] = 1 + nxtsum[i] / len(adjl)

v_prob = [0] * n
v_prob[0] = 1
for i, adjl in enumerate(v):
	count = len(adjl)
	for nxt in adjl:
		v_prob[nxt] += v_prob[i] / count

loss_max = 0
for i, adjl in enumerate(v):
	count = len(adjl)
	if count <= 1:
		continue
	for j in adjl:
		loss = e[i] - (1 + (nxtsum[i] - e[j]) / (count - 1))
		loss *= v_prob[i]
		if loss > loss_max:
			loss_max = loss

print(e[0] - loss_max)
