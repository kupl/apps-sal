n = int(input())
rng = [int(t) for t in input().split()]
ans = 0
while len(rng) != 0:
    mx = max(rng)
    if mx <= 0:
        break
    ans += mx
    rng.remove(mx)
    for i in range(len(rng)):
        if rng[i] == mx:
            rng[i] -= 1
print(ans)
