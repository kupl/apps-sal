def i_ints():
    return list(map(int, input().split()))


def next_free_from_blocks(n, blocks):
    """ n : pos ranges from 0 to n-1
        blocks: sorted list of blocked positions
        
        return a list that maps each position to the next higher non-blocked position
    """
    m = 0
    res = list(range(n+1))
    for i in reversed(blocks):
        res[i] = res[i+1]
        if res[i] - i > m:
            m = res[i] - i
    return res, m
    

#############

n, m, k = i_ints()

blocks = i_ints()
costs = i_ints()


next_free, max_block_len = next_free_from_blocks(n, blocks)
blocks.append(n+1)
if m == 0:
    max_block_len = 0
if max_block_len >= k or blocks[0] == 0:
    print(-1)
else:
    minimal_costs = [c * ((n+l-1)//l) for l, c in enumerate(costs, 1)]
    maximal_costs = [c * 2 * ((n+l)//(l+1)) for l, c in enumerate(costs, 1)]
    max_costs = min(maximal_costs[max_block_len:])
    
    possible = [i+1 for i in range(max_block_len, k) if minimal_costs[i] <= max_costs]
    for i in range(len(possible)-1)[::-1]:
        if costs[possible[i]-1] > costs[possible[i+1]-1]:
            del possible[i]
    
    def calc(l):
        """ for strength l, calculate  number of lamps needed """
        count = 1
        pos = n-l
        while pos > 0:
            pos = next_free[pos] - l
            count += 1
        return count
    
    
    print(min(calc(l) * costs[l-1] for l in possible))

