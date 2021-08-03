N, M = list(map(int, input().split()))
a_b_l = []
for _ in range(M):
    a_b_l.append(list(map(int, input().split())))

a_b_l = sorted(a_b_l, key=lambda x: x[1])
ans = 0
prev_removed_bridge = 0
for a, b in a_b_l:
    if a <= prev_removed_bridge:
        continue
    prev_removed_bridge = b - 1
    ans += 1
print(ans)
