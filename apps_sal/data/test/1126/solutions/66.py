n, x, m = map(int, input().split())
mod = [-1] * m
start = 0
last = 0
a = [x]
mod[x] = 0
for i in range(1, m):
    if i >= n:
        break
    a_new = a[-1]**2 % m
    if mod[a_new] == -1:
        mod[a_new] = i
    else:
        start = mod[a_new]
        last = i
        break
    a.append(a_new)

loop_num = 0
remain = 0
if last - start:
    loop_num = (n - start) // (last - start)
    remain = (n - start) % (last - start)
    out = sum(a[:start]) + sum(a[start:last + 1]) * loop_num
    out += sum(a[start:start + remain])
else:
    out = sum(a)

print(out)
