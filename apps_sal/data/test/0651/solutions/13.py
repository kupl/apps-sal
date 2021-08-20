import itertools as it
(n, m) = list(map(int, input().split()))
d = []
for i in range(n):
    d.append(input())
    if 'S' in d[-1]:
        s = [i, d[-1].index('S')]
    if 'E' in d[-1]:
        e = [i, d[-1].index('E')]
p = input()
dic = {'n': [-1, 0], 'e': [0, 1], 's': [1, 0], 'w': [0, -1]}
z = it.permutations('news', 4)
res = 0
for i in z:
    st = s
    et = e
    q = {'0123'[j]: dic[i[j]] for j in range(4)}
    for j in p:
        cur = q[j]
        st = [st[0] + cur[0], st[1] + cur[1]]
        if st[0] < 0 or st[0] >= n or st[1] < 0 or (st[1] >= m) or (d[st[0]][st[1]] == '#'):
            break
        if st == et:
            break
    if st == et:
        res += 1
print(res)
