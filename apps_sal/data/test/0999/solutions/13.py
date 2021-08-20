n = int(str(input()).strip())
min_i_r = 10 ** 9 + 1
max_i_l = 0
for _ in range(n):
    (l, r) = str(input()).strip().split(' ', 1)
    min_i_r = min(min_i_r, int(r))
    max_i_l = max(max_i_l, int(l))
m = int(str(input()).strip())
min_j_r = 10 ** 9 + 1
max_j_l = 0
for _ in range(m):
    (l, r) = str(input()).strip().split(' ', 1)
    min_j_r = min(min_j_r, int(r))
    max_j_l = max(max_j_l, int(l))
ans = max(max_j_l - min_i_r, max_i_l - min_j_r)
print(ans if ans > 0 else 0)
