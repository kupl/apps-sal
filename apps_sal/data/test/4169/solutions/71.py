N, M = list([int(n) for n in input().split(" ")])
E = []
for i in range(N):
    tmp = input().split(" ")
    E.append({
        "price": int(tmp[0]),
        "count": int(tmp[1])
    })

E.sort(key=lambda e: e["price"])

totP = 0
totC = 0
for i in range(len(E)):
    if totC + E[i]["count"] >= M:
        totP += (M - totC) * E[i]["price"]
        break
    else:
        totC += E[i]["count"]
        totP += E[i]["price"] * E[i]["count"]

print(totP)
