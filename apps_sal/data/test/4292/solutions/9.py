(n, k) = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
price = 0
for i in range(k):
    price += l[i]
print(price)
