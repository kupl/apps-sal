from collections import defaultdict
import bisect
def solve():
    s = input()
    t = input()
    d = defaultdict(list)
    st_s = set(s)

    for i in range(len(s)):
        d[s[i]].append(i)
    
    round = 0
    prev = -1
    for i in range(len(t)):
        if not t[i] in st_s:
            print(-1)
            return
        now = getNextIdx(prev,d[t[i]])
        if now <= prev:
            round += 1
        
        prev = now
    
    print(prev + round*len(s) + 1)

def getNextIdx(prev,idx_list):
    ret_idx = bisect.bisect_right(idx_list, prev)
    if ret_idx == len(idx_list):
        return idx_list[0]

    return idx_list[ret_idx]

def __starting_point():
    solve()
__starting_point()
