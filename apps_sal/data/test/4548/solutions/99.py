(n, m, x) = map(int, input().split())
a = list(map(int, input().split()))
k = [0] * (n + 1)
for i in a:
    k[i] = 1
print(min(sum(k[0:x + 1]), sum(k[x:n + 1])))
