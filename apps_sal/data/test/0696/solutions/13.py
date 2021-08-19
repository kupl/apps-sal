p = int(input())
ans = 0
for i in range(1, p):
    t = 1
    for j in range(1, p - 1):
        t = t * i % p
        if (t - 1) % p == 0:
            break
    else:
        t = t * i % p
        if (t - 1) % p == 0:
            ans += 1
print(ans)
