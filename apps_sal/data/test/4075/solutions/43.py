from itertools import product
(n, m) = map(int, input().split())
switches = []
for _ in range(m):
    x = list(map(int, input().split()))[1:]
    temp = []
    for i in range(n):
        if i + 1 in x:
            temp.append(1)
        else:
            temp.append(0)
    switches.append(temp)
p = list(map(int, input().split()))
ans = 0
for on_off in product([1, 0], repeat=n):
    flag = 1
    for (i, switch) in enumerate(switches):
        cnt = 0
        for (x, y) in zip(on_off, switch):
            if x == 1 and y == 1:
                cnt += 1
        if cnt % 2 != p[i]:
            flag = 0
    if flag:
        ans += 1
print(ans)
