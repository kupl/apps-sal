def distance(b, a, n):
    return b - a if b >= a else b + n - a


n, m = list(map(int, input().split()))
dic_last_candy = dict()
dict_node = dict()
s = ''
for i in range(m):
    a, b = list(map(int, input().split()))
    c = dict_node.get(a, 0)
    c += 1
    dict_node[a] = c
    last_candy = dic_last_candy.get(a, 0)
    if last_candy:
        c1 = distance(last_candy, a, n)
        c2 = distance(b, a, n)
        if c2 < c1:
            last_candy = b
    else:
        last_candy = b
    dic_last_candy[a] = last_candy

for i in range(1, n + 1):
    c = dict_node.get(i, 0)
    if c:
        now_step = (c - 1) * n + distance(dic_last_candy[i], i, n)
        dict_node[i] = now_step
s = ''
for i in range(1, n + 1):
    now_step = dict_node.get(i, 0)
    min_step = now_step
    for j in range(1, n + 1):
        if dict_node.get(j, 0):
            now_step = dict_node.get(j, 0) + distance(j, i, n)
            if min_step < now_step:
                min_step = now_step
    s += ' ' + str(min_step)
print(s[1:])
