import math
s = input()
l = s.split()
(n, m, k) = (int(i) for i in l)
s = input()
a = s.split()
s = input()
b = s.split()
h1 = [0 for i in range(0, 100001)]
h2 = [0 for i in range(0, 100001)]
count = 1
for i in a:
    t_n = int(i)
    h1[t_n] = int(math.ceil(count / k))
    h2[t_n] = count % k
    if h2[t_n] == 0:
        h2[t_n] = k
    count += 1
ans = 0
for i in b:
    num = int(i)
    ans += h1[num]
    if h2[num] == 1 and h1[num] == 1:
        continue
    elif h2[num] == 1:
        cn = k * (h1[num] - 1) + h2[num] - 1
        h1[int(a[cn - 1])] += 1
        h2[int(a[cn - 1])] = 1
        h1[num] -= 1
        h2[num] = k
        (a[cn - 1], a[cn]) = (a[cn], a[cn - 1])
    else:
        cn = k * (h1[num] - 1) + h2[num] - 1
        h2[num] -= 1
        h2[int(a[cn - 1])] += 1
        (a[cn - 1], a[cn]) = (a[cn], a[cn - 1])
print(ans)
