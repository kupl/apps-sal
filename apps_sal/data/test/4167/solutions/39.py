n, k = map(int, input().split())
mod_0 = 0
mod_harf = 0

for i in range(1, n + 1):
    if i % k == 0:
        mod_0 += 1
    elif i % k == (-i) % k:
        mod_harf += 1

res = mod_0 ** 3 + mod_harf ** 3
print(res)
