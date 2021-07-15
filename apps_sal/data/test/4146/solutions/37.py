n = int(input())
l = list(map(int, input().split()))
a = {}
b = {}
for i in range(n // 2):
    key_a = l[i * 2]
    key_b = l[i * 2 + 1]
    if key_a in a:
        a[key_a] = a[key_a] + 1
    else:
        a[l[i * 2]] = 1
    if key_b in b:
        b[key_b] = b[key_b] + 1
    else:
        b[key_b] = 1
a = sorted(a.items(), key=lambda x: x[1], reverse=True)
b = sorted(b.items(), key=lambda x: x[1], reverse=True)
# a = list(a.items())
# b = list(b.items())
# print(a)
# print(b)
ca_max = a[0][0]
cb_max = b[0][0]
ca_max_num = a[0][1]
cb_max_num = b[0][1]
same_num = ca_max_num + cb_max_num
if ca_max == cb_max:
    if len(a) > 1:
        next_ca_max = a[1][1]
    else:
        next_ca_max = 0
    if len(b) > 1:
        next_cb_max = b[1][1]
    else:
        next_cb_max = 0
    same_num = max(ca_max_num + next_cb_max, cb_max_num + next_ca_max)
print(n - same_num)
