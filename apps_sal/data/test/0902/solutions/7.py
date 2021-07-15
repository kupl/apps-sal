(n, k) = [int(x) for x in input().split(' ')] 
a = [ int(x) for x in input().split(' ')]
if k >= 10 * (n - 1):
    print(max(a))
else:
    winner = a.pop(0)
    
    conseq_win = 0
    while conseq_win != k:
        u = winner
        v = a.pop(0)
        if u > v:
            a.append(v)
            conseq_win = conseq_win + 1
        else:
            a.append(u)
            winner = v
            conseq_win = 1
    print(winner)
