def get_input_list():
    return list(map(int, input().split()))


n = int(input())
l = []
r = []
for _ in range(n):
    (li, ri) = get_input_list()
    l.append(li)
    r.append(ri)
l.sort()
r.sort()
res = n
for i in range(n):
    res += max(l[i], r[i])
print(res)
