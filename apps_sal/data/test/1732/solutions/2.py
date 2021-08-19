# D
input()
ok = {0: 0}
for p, c in zip(list(map(int, input().split())),
                list(map(int, input().split()))):
    ad = []
    for b, u in list(ok.items()):
        a = p
        while b:
            a, b = b, a % b
        ad.append((a, u + c))
    for a, u in ad:
        ok[a] = min(u, ok.get(a, 1000000000))
print(ok.get(1, -1))
