a = list(map(int, input().split()))
N = a[0]
K = a[1]
p = list(map(int, input().split()))

p.sort()
x = 0

for i in range(K):
    x += p[i]
print(x)
