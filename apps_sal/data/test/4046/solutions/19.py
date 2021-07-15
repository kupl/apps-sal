
n = int(input())
a = [int(i) for i in input().split()]
st = 0
b = [st]
mx = st
for el in a:
    st += el
    mx = max(st, mx)
    b.append(st)
x = n - 1 - mx
used = [1] * n
for el in b:
    if 0 <= el + x <= n - 1:
        used[el + x] = 0
    else:
        print(-1)
        return
if sum(used) == 0:
    for el in b:
        print(el + x + 1, end = ' ')
else:
    print(-1)
