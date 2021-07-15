n = int(input())
a = [int(x) for x in input().split()]
maxi = 0
for i in a:
    maxi = max(maxi, a.count(i))
print(maxi)
