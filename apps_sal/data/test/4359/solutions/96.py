V = [int(input()) for _ in range(5)]
v_mod = [x % 10 if x % 10 != 0 else 10 for x in V]
min_mod = min(v_mod)
ans = 0
for (i, v) in enumerate(V):
    ans += v + (10 - v_mod[i])
ans -= 10 - min_mod
print(ans)
