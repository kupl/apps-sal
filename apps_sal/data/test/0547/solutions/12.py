(n, k) = tuple(map(int, input().split()))
ls = [set() for i in range(1, 110)]
for i in range(n):
    s = input().strip()
    ls[len(s)].add(s)
key = input().strip()
kl = len(key)
kk = 0
for i in range(1, kl):
    kk += len(ls[i])
bt = kk + kk // k * 5 + 1
ft = kk + len(ls[kl]) + (kk + len(ls[kl]) - 1) // k * 5
print(bt, ft)
