(n, x, m) = map(int, input().split())
mod = [-1] * m
start = 0
end = 0
a = [x]
mod[x] = 0
for i in range(1, m):
    if i >= n:
        break
    a_new = a[-1] ** 2 % m
    if mod[a_new] == -1:
        mod[a_new] = i
    else:
        start = mod[a_new]
        end = i
        break
    a.append(a_new)
loop_num = 0
last_num = 0
if end - start:
    loop_num = (n - start) // (end - start)
    last_num = (n - start) % (end - start)
    out = sum(a[:start]) + sum(a[start:end + 1]) * loop_num
    out += sum(a[start:start + last_num])
else:
    out = sum(a)
print(out)
