N, K = [int(s) for s in input().split()]
ls = [int(s) for s in input().split()]
town = set()
town.add(1)
town_ls = [1]
now = 1
for i in range(min([K, N])):
    now = ls[now - 1]
    if now in town:
        break
    town.add(now)
    town_ls.append(now)

if i + 1 == K:
    print(now)
else:
    L = i + 1
    S = town_ls.index(now)
    loop = L - S
    # print(loop,S)
    x = (K - S) % loop + S
    print(town_ls[x])
