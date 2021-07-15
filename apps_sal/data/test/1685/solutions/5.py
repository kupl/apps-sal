from math import log
n, q = [int(i) for i in input().split()]
maxlvl = int(log(n + 1, 2)) + 1
pows = [2 ** i for i in range(maxlvl)]

def calc_lvl(m):
    for lvl in range(1, maxlvl):
        if (m - pows[lvl-1]) % pows[lvl] == 0:
            return (lvl, ((m - pows[lvl-1]) % (2 * pows[lvl]) == 0))

for i in range(q):
    start = int(input())
    query = input()
    lvl, ind = calc_lvl(start)
    
    for c in query:
        if c == 'U':  
            if start == pows[-2]:
                continue
            start += (1 if ind else -1) * pows[lvl - 1]
            lvl, ind = calc_lvl(start)    
        else:
            if start % 2 != 0:
                continue
            start += (1 if c == 'R' else -1) * pows[lvl - 2]
            lvl, ind = lvl - 1, int((c == 'L'))
            
    print(start)
            
                
                

            

