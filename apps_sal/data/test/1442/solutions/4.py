n, s = map(int, input().split())
pricesell = dict()
pricebuy = dict()
sellp = set()
buyp = set()
for i in range(n):
    tmp = input().split()
    if tmp[0] == "B":
        if int(tmp[1]) in buyp:
            pricebuy[int(tmp[1])] += int(tmp[2])
        else:
            pricebuy[int(tmp[1])] = int(tmp[2])
        buyp.add(int(tmp[1]))
    else:
        if int(tmp[1]) in sellp:
            pricesell[int(tmp[1])] += int(tmp[2])
        else:
            pricesell[int(tmp[1])] = int(tmp[2])
        sellp.add(int(tmp[1]))
buy = list(pricebuy.items())
sell = list(pricesell.items())
buy.sort(reverse=True)
sell.sort()
buy1 = buy[:min(s, len(buy))]
sell1 = sell[:min(s, len(sell))]
sell1.sort(reverse=True)
buy1 = list(map(lambda x: "B " + str(x[0]) + " " + str(x[1]), buy1))
sell1 = list(map(lambda x: "S " + str(x[0]) + " " + str(x[1]), sell1))
print(*sell1, sep="\n")
print(*buy1, sep="\n")
