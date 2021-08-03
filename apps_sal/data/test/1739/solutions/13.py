n, x = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)
biggest = max(a)

exp = total - biggest

hm = a.count(biggest)
while hm % x == 0:
    biggest -= 1
    exp += 1
    hm = hm // x + a.count(biggest)

if exp > total:
    exp = total
print(pow(x, exp, 1000000007))
