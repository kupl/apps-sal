n = int(input())
legs = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
legs.sort(key=lambda x: x[1], reverse=True)
# print(legs)
cnt = {}
s = 0
for i in range(n):
    s += legs[i][1]
    if legs[i][0] not in cnt:
        cnt[legs[i][0]] = [1, legs[i][1]]
    else:
        cnt[legs[i][0]][0] += 1
        cnt[legs[i][0]][1] += legs[i][1]

temp = sorted(cnt.items())
mn = 9999999999999
f = 0
while temp:
    l, t = temp.pop()
    c, e = t
    s -= e
    val = s
    i = 0
    count = 0
    while count < c - 1:
        if legs[i][0] < l:
            count += 1
            val -= legs[i][1]
        i += 1
        if i == n:
            break
    # print(l, c, e, val+f)
    if val + f < mn:
        mn = val + f
    f += e
print(mn)
