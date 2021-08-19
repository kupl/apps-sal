n, x = list(map(int, input().split()))
a = [int(x) for x in input().split()]
ad = {}
count = 0
for i in a:
    count += ad.get(i ^ x, 0)
    ad[i] = ad.get(i, 0) + 1
# print(ad)
print(count)
