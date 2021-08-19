(v1, v2) = list(map(int, input().split()))
(t, d) = list(map(int, input().split()))
L1 = [0] * t
L2 = [0] * t
L1[0] = v1
for i in range(1, t):
    L1[i] = L1[i - 1] + d
j = t - 2
L2[j + 1] = v2
while j >= 0:
    L2[j] = L2[j + 1] + d
    j -= 1
ans = 0
for i in range(0, t):
    ans += min(L1[i], L2[i])
print(ans)
