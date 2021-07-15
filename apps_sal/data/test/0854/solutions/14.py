import random

n, t = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

#n = 2*(10**5)
#t = random.randint(10**17, 10**18)
#a = [random.randint(1, 10**9) for i in range(n)]

tot = sum(a)
candies = 0

def solve(cur, nxt, l):
    if l<=0: return
    nonlocal candies
    nonlocal t
    nonlocal tot
    nxt = []
    revs = t//tot
    candies += (revs*l)
    t -= (revs*tot)
    for cost in cur:
        if cost <= t:
            t-=cost
            candies+=1
            nxt.append(cost)
        else:
            tot -= cost
            l-=1
    solve(nxt, cur, l)
                        
solve(a, [], n)
print(candies)

