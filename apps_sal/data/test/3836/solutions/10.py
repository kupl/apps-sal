n = int(input())
a, b, c = [], [], []
ans = 0
num11 = 0
for i in range(n):
    t, val = map(int, input().split())
    if t == 11:
        ans += val
        num11 += 1
        continue
    if t & 1:
        a.append(val)
    if t & 2:
        b.append(val)
    if not t:
        c.append(val)
a.sort(reverse=True)
b.sort(reverse=True)

min_num = min(len(a), len(b))
ans += sum(a[:min_num]) + sum(b[:min_num])
t = a[min_num:] + b[min_num:] + c
t.sort(reverse=True)
ans += sum(t[:2 * (min(len(a), len(b)) + num11) - 2 * min_num - num11])
print(ans)
