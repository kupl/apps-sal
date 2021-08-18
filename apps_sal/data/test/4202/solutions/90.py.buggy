l, r = map(int, input().split())
l_mod = l % 2019
r_mod = r % 2019
if l + 2019 <= r:
    print(0)
    return
m = 3000
for i in range(l_mod, r_mod + 1):
    for j in range(i + 1, r_mod + 1):
        m = min(m, i * j % 2019)
print(m)
