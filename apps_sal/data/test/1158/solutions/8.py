(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
mx = 0
p = set(a)
for i in p:
    b = a.count(i)
    if b > mx:
        mx = b
blud = -(-mx // k)
print(blud * k * len(p) - len(a))
