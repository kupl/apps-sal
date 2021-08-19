(N, K) = [int(x) for x in input().split()]
td = [0] * N
for i in range(N):
    td[i] = [int(x) for x in input().split()]
td = sorted(td, reverse=True)
var_p1 = [0] * N
var_p0 = [0] * N
n_p1 = 0
n_p0 = 0
for i in range(N):
    if i == 0 or (i > 0 and td[i][0] != td[i - 1][0]):
        var_p1[n_p1] = td[i][1]
        n_p1 += 1
    else:
        var_p0[n_p0] = td[i][1]
        n_p0 += 1
var_p1.sort(reverse=True)
var_p0.sort(reverse=True)
val_taste = sum(var_p0[0:K])
val_vars = 0
ans = 0
for j in range(1, K + 1):
    val = var_p1[j - 1]
    if val <= 0:
        break
    val_taste = val_taste + val - var_p0[K - j]
    val_vars = j * j
    ans = max(ans, val_taste + val_vars)
print(ans)
