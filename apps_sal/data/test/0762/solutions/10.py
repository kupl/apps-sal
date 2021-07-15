n, b = [int(c) for c in input().split(" ")]
a = [int(c) for c in input().split(" ")]

evenodd = []

evenodd_cur = 0
for i in range(n):
    if a[i] % 2 == 0: evenodd_cur += 1
    else: evenodd_cur -= 1
    evenodd.append(evenodd_cur)

watchlist = []
for i in range(n-1):
    if evenodd[i] == 0:
        watchlist.append((abs(a[i] - a[i+1]), i))

watchlist.sort()
# print(watchlist)

totalcount = 0
for price, index in watchlist:
    if b >= price:
        totalcount += 1
        b -= price
    else:
        break

print(totalcount)
