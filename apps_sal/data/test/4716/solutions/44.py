(n, k) = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)
x = 0
for i in range(-1, -1 - k, -1):
    x += l[i]
print(x)
