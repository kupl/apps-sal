N, K = list(map(int, input().split()))
V = list(map(int, input().split()))
left = [0] * (K + 1)
right = [0] * (K + 1)

for k in range(1, min(N + 1, K + 1)):
    max_vk = 0
    for j in range(k // 2 + 1):
        push = j
        pop = k - j
        # print(k,pop,push)
        if pop > N:
            continue
        else:
            tmp = sum(sorted(V[:pop])[push:])
        max_vk = max(max_vk, tmp)
    left[k] = max_vk

Vrev = V[::-1]

for k in range(1, K + 1):
    max_vk = 0
    for j in range(k // 2 + 1):
        push = j
        pop = k - j
        # print(k,pop,push)
        if pop > N:
            continue
        else:
            tmp = sum(sorted(Vrev[:pop])[push:])
        max_vk = max(max_vk, tmp)
    right[k] = max_vk

for i in range(len(right) - 1):
    if right[i + 1] < right[i]:
        right[i + 1] = right[i]
    if left[i + 1] < left[i]:
        left[i + 1] = left[i]

ans = 0
NK = K
max_ans = 0
for v in V:
    if v > 0:
        max_ans += v

for i in range(NK + 1):
    ans = max(ans, right[i] + left[NK - i])

print((min(max_ans, ans)))
