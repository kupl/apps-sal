n = int(input())
m = 998244353
dl = [1] + [0] * n;
for i in map(int, input().split()):
    v = dl[:]
    if(0 < i < n):
        v[i] = (v[i] + v[0]) % m
    for j in range(n):
        v[j] = (v[j] + dl[j + 1]) % m
    dl = v
print((dl[0] - 1) % m)
