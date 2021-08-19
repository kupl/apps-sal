(n, v) = list(map(int, input().split()))
sellers = []
for i in range(n):
    auctions = list(map(int, input().split()))
    k = auctions[0]
    for j in range(k):
        if v > auctions[1 + j]:
            sellers.append(str(i + 1))
            break
print(len(sellers))
print(' '.join(sellers))
