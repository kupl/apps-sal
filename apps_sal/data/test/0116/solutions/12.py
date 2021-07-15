l_1, r_1, l_2, r_2, k = list(map(int, input().split()))
ans = min(r_1, r_2) - max(l_1, l_2) + 1
if max(l_1, l_2) <= k <= min(r_1, r_2):
    ans -= 1
if ans < 0:
    ans = 0
print(ans)

