(l, r, a) = [int(x) for x in input().split()]
maxi = max(l, r)
mini = min(l, r)
while mini != maxi and a != 0:
    a -= 1
    mini += 1
while a // 2 > 0:
    mini += 1
    maxi += 1
    a -= 2
maxi = mini
print(mini + maxi)
