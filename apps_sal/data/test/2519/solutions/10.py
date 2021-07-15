def f(x):
    x = int(x)
    return x*(x+1)//2/x

n, k = list(map(int, input().split()))
p = list(map(f, input().split()))

s = sum(p[:k])
a = s
for i in range(k, len(p)):
    s += p[i] - p[i-k]
    a = max(a, s)

print(a)

