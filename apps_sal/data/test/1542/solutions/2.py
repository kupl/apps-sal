from bisect import bisect
n = int(input())
shops = [int(i) for i in input().split()]
shops.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect(shops, m))

