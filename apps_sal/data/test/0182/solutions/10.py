has = list(map(int, input().split()))
target = list(map(int, input().split()))

offer = []
for i in range(3):
    if has[i] - target[i] > 0:
        offer.append(int((has[i] - target[i]) / 2))
    else:
        offer.append(int(has[i] - target[i]))

if sum(offer) >= 0:
    print("Yes")
else:
    print("No")
