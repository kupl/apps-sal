cards = list(map(int, input().split()))
zmensenie = 0
for card in cards:
    oc = 0
    for c2 in cards:
        if c2 == card:
            oc += 1
    if oc >= 2:
        oc = min(oc, 3)
        zmensenie = max(zmensenie, oc * card)
print(sum(cards) - zmensenie)
