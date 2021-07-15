n, p = [int(i) for i in input().split()]
kek = [0] * n
lol = [0] * n
for i in range(n):
    l, r = [int(i) for i in input().split()]
    a = ((r // p + 1) * p - l // p * p) // p
    if l % p:
        a -= 1
    lol[i] = r - l + 1
    kek[i] = a
ans = 0
for i in range(n):
    t = (i + 1) % n
    ans += ((kek[i] * (lol[t] - kek[t]) + kek[t] * (lol[i] - kek[i]) + kek[i] * kek[t]) * 2000) / (lol[i] * lol[t])
print(ans)
