def counter(s, t): ## O(n**2) potentially oops

    how_many = 0

    for i in range(0, len(s)-len(t)+1):

        ## print(i, i+len(t))

        if s[i:i+len(t)] == t:
            how_many += 1

    return how_many

while True:
    
    inp = input().split()

    n = int(inp[0])
    k = int(inp[1])

    s = input()

    returning = s

    for i in range(1, n+1):
        if counter(returning+s[-i:], s) > counter(returning, s): ## (returning + s[-i:]).count(s) > returning.count(s):
            addition = s[-i:]
            break

    returning = s + (k-1)*addition

##    while counter(returning, s) < k: ## returning.count(s) < n:
##
##        for i in range(1, n+1):
##
##            if counter(returning+s[-i:], s) > counter(returning, s): ## (returning + s[-i:]).count(s) > returning.count(s):
##
##                returning += s[-i:]
##                break

    print(returning)

    break

