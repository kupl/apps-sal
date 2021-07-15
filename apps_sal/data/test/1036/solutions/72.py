n,k = map(int, input().split())
s = input()

def f(h1,h2):
    if h1==h2:
        return h1
    if h1=="P":
        if h2=="R":
            return "P"
        else:
            return "S"
    if h1=="R":
        if h2=="S":
            return "R"
        else:
            return "P"
    if h1=="S":
        if h2=="P":
            return "S"
        else:
            return "R"

def solve(hands,k):
    while k>0:
        hands=nxt(hands)
        k-=1
#        print(hands,k)
    print(hands[0])

def nxt(hands):
    hands+=hands
    n_hand=[]
    for i in range(len(hands)//2):
        win = f(hands[2*i], hands[2*i+1])
        n_hand.append(win)

    return n_hand

solve(s,k)
