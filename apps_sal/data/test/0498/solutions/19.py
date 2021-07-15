n, m, k = list(map(int, input().split()))

r = -(-k // (2*m))
lr = ['R', 'L'][k%2]
pos = k % (2*m) if k % (2*m) else 2*m
d = (pos+1) // 2

print(r, d, lr)

