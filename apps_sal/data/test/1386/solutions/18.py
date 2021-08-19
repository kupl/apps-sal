(w, h) = map(int, input().split())
p = 998244353
k = 1
for i in range(w + h):
    k = 2 * k % p
print(k)
