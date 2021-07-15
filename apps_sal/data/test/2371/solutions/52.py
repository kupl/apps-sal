n, z, w = map(int, input().split())
cards = list(map(int, input().split()))
#print(getX(z, w, cards, 0))
if(abs(cards[len(cards)-1]-w)>abs(cards[len(cards)-1]-cards[len(cards)-2])):
    print(abs(cards[len(cards)-1]-w))
else:
    print(abs(cards[len(cards)-1]-cards[len(cards)-2]))
