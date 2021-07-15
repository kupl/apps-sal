import sys

TESTING = False

def solve():
    start, = read()
    costs = read()
    scosts = [(x+1, costs[x]) for x in range(len(costs))]
    scosts.sort(reverse = True)
    mincost = scosts[0][1]
    minnum = scosts[0][0]
    for val, cost in scosts:
        if cost < mincost:
            mincost = cost
            minnum = val
    best = [minnum for x in range(start//mincost)]
    rem = start - (start//mincost)*mincost
    for i in range(len(best)):
        changed = False
        for val, cost in scosts:
            if val > best[i] and (cost-mincost) <= rem:
                rem += mincost
                rem -= cost
                best[i] = val
                changed = True
                break
        if not changed:
            break
    if len(best) == 0: return -1
    else:
        ans = ''.join(map(str,best))
        return ans







def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

def run():
    if TESTING: sys.stdin  = open("test.txt")
    res = solve()
    write(res)
run()
