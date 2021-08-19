n = int(input())
p = [int(input()) for i in range(n)]
k = 0
m = max(p)
l = int(m / 2)
for i in p:
    k = k + i
print(k - l)
