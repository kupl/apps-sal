n = int(input())
cards = list(map(int,input().split()))
cards = sorted(cards,reverse=True)
alice = bob = 0
for i in cards[::2]:
    alice += i
for j in cards[1::2]:
    bob += j
print(alice - bob)
