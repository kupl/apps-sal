n = int(input())
l = list(map(int, input().split()))
l.sort()
# print(l)
ll = l.copy()
up = 1
left = l[0]
for i in range(n):
    if l[i] > left + 2:
        left = l[i]
        up += 1
# print(up)
# print(ll)
ll[0] -= 1
# print(ll)
for i in range(1, n - 1):
    if ll[i - 1] == ll[i]:
        if ll[i] != ll[i + 1]:
            ll[i] += 1
    elif ll[i - 1] == ll[i] - 1:
        continue
    else:
        ll[i] -= 1
    # print(ll)
ll[n - 1] += 1
# print(ll)
d = {}
for i in ll:
    d[i] = 0
najw = len(d)
print(up, najw)
