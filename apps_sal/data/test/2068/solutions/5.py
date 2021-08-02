n, qwe = int(input()), {'polycarp': 1}
for _ in range(n):
    t = input().split(' reposted ')
    qwe[t[0].lower()] = qwe[t[1].lower()] + 1
print(max(qwe.values()))
